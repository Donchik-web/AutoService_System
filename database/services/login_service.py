from database.tables import Users
from database.connection import Session
from app.utils.password_utils import check_existing_password


def login_user(user_email, user_password):
    try:
        with Session() as session:
            existing_user = session.query(Users).filter(Users.email == user_email).first()
            if existing_user:
                if check_existing_password(password=user_password, hashed_password=existing_user.password):
                    user_id = existing_user.id
                    return True, "Вы вошли в свой аккаунт!", user_id
            return False, "Неверный email или пароль!", None
    except Exception as e:
        return False, f"Неожиданная ошибка {e}", None


def get_user_by_id(user_id):
    try:
        with Session() as session:
            user = session.query(Users).filter(Users.id == user_id).first()
            if user:
                user_data = {
                    "user_name": user.name,
                    "user_surname": user.surname,
                    "user_email": user.email,
                    "hash_password": user.password,
                }
                return True, user_data
            return False, "Пользователь не найден"
    except Exception as e:
        return False, f"Неожиданная ошибка {e}"
