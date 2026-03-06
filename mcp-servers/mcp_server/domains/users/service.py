# services/user_service.py

def get_user_by_id(user_id: str):
    fake_db = {
        "u1": {"id": "u1", "name": "Edmund", "role": "admin"},
        "u2": {"id": "u2", "name": "Jonathan", "role": "user"},
    }

    return fake_db.get(user_id, None)