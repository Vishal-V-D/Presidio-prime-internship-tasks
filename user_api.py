from user_model import User

def create_user(user_id, name, email):
    return User(user_id, name, email)

def get_user_info(user):
    return {
        "user_id": user.user_id,
        "name": user.name,
        "email": user.email
    }

def get_user_contact_info(user):
    return user.get_contact_info()

# 🆕 New function
def update_user_email(user, new_email):
    user.email = new_email
    return user
