from models.database import db
from models.users import Users
from argon2 import PasswordHasher
ph = PasswordHasher()


def get_user(**kwargs):
    for key, value in kwargs.items():
        if key == "id":
            return db.session.query(Users).filter_by(id=value).first()
        elif key == "seq":
            return db.session.query(Users).filter_by(seq=value).first()


def set_password(user, password):
    user.password = ph.hash(password)
    db.session.commit()


def verify_password(user, password):
    try:
        ph.verify(user.password, password)
        return True
    except Exception:
        return False
