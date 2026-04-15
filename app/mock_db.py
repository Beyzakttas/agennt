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
    "TRX-002": "Yetersiz bakiye ve şüpheli giriş.",
    "TRX-003": "Hesap dondurulduğu için işlem reddedildi."
}