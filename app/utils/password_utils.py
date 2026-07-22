import bcrypt


def hash_password(password: str) -> str:
    """Хеширование пароля"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_existing_password(password: str, hashed_password: str) -> bool:
    """Сравнение введенного пароля при входе в аккаунт"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


