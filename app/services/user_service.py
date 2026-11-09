from app.extensions import db
from app.models.user import User


def get_by_email(email: str) -> User:
    return User.query.filter_by(email=email).first()

def register_user(email: str, password: str) -> User | None:
    if get_by_email(email):
        return None
    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

def authenticate(email: str, password: str) -> User | None:
    user = get_by_email(email)
    if user and user.check_password(password):
        return user
    return None