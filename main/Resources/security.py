from werkzeug.security import check_password_hash
from .users import User


def authenticate(username, password):
    user = User.find_by_username(username)
    if user and check_password_hash(user.password, password):
        return user
    else:
        print("Incorrect login name or password. Please try again.")
        # return {'log in error': 'Incorrect login name or password. Please try again.'}, 400


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)