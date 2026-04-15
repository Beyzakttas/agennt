import requests
from app.tools import get_user, get_transactions, get_fraud_reason

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen:4b"


def ask_llm(prompt: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


def run_agent(text: str):

    # email çek
    email = None
    for word in text.split():
        if "@" in word:
            email = word.strip()
            break

    if not email:
        return "Email bulunamadı"

    user = get_user(email)
    if not user:
        return "User not found"

    txs = get_transactions(user["id"])

    failed = [t for t in txs if t["status"] == "failed"]

    if not failed:
        return "Başarısız işlem yok"

    tx = failed[0]
    reason = get_fraud_reason(tx["id"])

    prompt = f"""
Kullanıcı: {email}
İşlem ID: {tx['id']}
Sebep: {reason}

Bunu kullanıcıya sade Türkçe açıkla.
"""

    return ask_llm(prompt)