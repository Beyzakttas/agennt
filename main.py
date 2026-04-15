import re
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Banka AI (No LangChain)")

# --- MOCK DB ---
MOCK_USERS = {
    "ali@sirket.com": {"id": "USR-101", "status": "active"},
    "ayse@sirket.com": {"id": "USR-102", "status": "suspended"}
}

MOCK_TRANSACTIONS = {
    "USR-101": [
        {"id": "TRX-001", "amount": 500, "status": "success"},
        {"id": "TRX-002", "amount": 1200, "status": "failed"}
    ],
    "USR-102": [
        {"id": "TRX-003", "amount": 2500, "status": "failed"}
    ]
}

MOCK_FRAUD_REASONS = {
    "TRX-002": "Yetersiz bakiye ve şüpheli konumdan giriş denemesi.",
    "TRX-003": "Hesap dondurulduğu için işlem reddedildi."
}

# --- REQUEST MODEL ---
class UserMessage(BaseModel):
    text: str = Field(..., min_length=3)

# --- EMAIL EXTRACTOR ---
def extract_email(text: str) -> Optional[str]:
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match.group(0).lower() if match else None

# --- CORE LOGIC ---
def analyze_payment_issue(text: str) -> str:
    email = extract_email(text)

    if not email:
        return "Lütfen işlemi kontrol edebilmem için e-posta adresinizi belirtiniz."

    # 1. Kullanıcı bul
    user = MOCK_USERS.get(email)
    if not user:
        return f"{email} adresine ait bir hesap bulunamadı."

    user_id = user["id"]

    # 2. İşlemleri al
    transactions = MOCK_TRANSACTIONS.get(user_id, [])
    if not transactions:
        return "Bu kullanıcıya ait işlem bulunamadı."

    # 3. Failed işlemi bul
    failed_tx = next((tx for tx in transactions if tx["status"] == "failed"), None)

    if not failed_tx:
        return "Başarısız işlem bulunamadı."

    # 4. Sebep bul
    reason = MOCK_FRAUD_REASONS.get(failed_tx["id"], "Bilinmeyen bir hata oluştu.")

    return (
        f"İşleminiz analiz edildi.\n\n"
        f"İşlem ID: {failed_tx['id']}\n"
        f"Tutar: {failed_tx['amount']} TL\n"
        f"Durum: Başarısız\n\n"
        f"Neden: {reason}"
    )

# --- API ---
@app.post("/ask")
async def ask(message: UserMessage):
    try:
        result = analyze_payment_issue(message.text)
        return {"answer": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"status": "API çalışıyor 🚀"}