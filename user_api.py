
from user_model import User

def create_user(user_id, name, email):
    return User(user_id, name, email)

def get_user_info(user):
    return {
        "user_id": user.user_id,
        "name": user.name,
        "email": user.email
    }
