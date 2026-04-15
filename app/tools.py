from app.mock_db import MOCK_USERS, MOCK_TRANSACTIONS, MOCK_FRAUD_REASONS


def get_user(email: str):
    user = MOCK_USERS.get(email)
    if not user:
        return None
    return user


def get_transactions(user_id: str):
    return MOCK_TRANSACTIONS.get(user_id, [])


def get_fraud_reason(tx_id: str):
    return MOCK_FRAUD_REASONS.get(tx_id, "Sebep bulunamadı")