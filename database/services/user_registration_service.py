from database.connection import Session
from database.tables import Users
from datetime import datetime, timezone
import uuid


def create_user_account(user_id, user_name, user_surname, user_email, hash_pwd):
    try:
        with Session() as session:
            existing_user = session.query(Users).filter(Users.email == user_email).first()
            if existing_user:
                return None, f"""
Регистрация не удалась!
Пользователь с таким email: {user_email} уже существует!"""

            if isinstance(user_id, uuid.UUID):
                user_id = str(user_id)

            user = Users(
                id=user_id,
                name=user_name,
                surname=user_surname,
                email=user_email,
                password=hash_pwd,
                created_at=datetime.now(timezone.utc)
            )

            session.add(user)
            session.commit()

            return True, f"""
Регистрация прошла успешно!
Добро пожаловать, {user_name} {user_surname}!
Вы создали аккаунт.
"""

    except Exception as e:
        print(f"Общая ошибка: {e}")
        return None, f"Ошибка при создании аккаунта: {str(e)}"
