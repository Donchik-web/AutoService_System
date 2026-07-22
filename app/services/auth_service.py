from uuid import uuid4
from PyQt6.QtWidgets import QMessageBox

from app import app_state
from app.utils.password_utils import hash_password
from database.services.user_registration_service import create_user_account
from app.utils.navigation_manager import close_reg_or_login_open_car_parameters


def processing_registration_data(name_le, surname_le, email_le, code_le, pwd_le, email_code_users):
    """Проверка введенных данных пользователем и их обработка"""
    name = name_le.text().strip()
    surname = surname_le.text().strip()
    email = email_le.text().strip()
    code_text = code_le.text().strip()
    pwd = pwd_le.text()

    if not name:
        QMessageBox.warning(name_le.window(), "Ошибка", "Введите имя")
        return

    if not surname:
        QMessageBox.warning(surname_le.window(), "Ошибка", "Введите фамилию")
        return

    if not email or "@" not in email:
        QMessageBox.warning(email_le.window(), "Ошибка", "Введите корректный e‑mail")
        return

    if not code_text:
        QMessageBox.warning(code_le.window(), "Ошибка", "Введите код подтверждения")
        return

    try:
        code = int(code_text)
    except ValueError:
        QMessageBox.warning(code_le.window(), "Ошибка", "Код должен быть числом")
        return

    if code != email_code_users.get(email, None):
        QMessageBox.warning(pwd_le.window(), "Ошибка", "Неверный код")
        return

    if not pwd:
        QMessageBox.warning(pwd_le.window(), "Ошибка", "Введите пароль")
        return
    if len(pwd) < 8:
        QMessageBox.warning(pwd_le.window(), "Ошибка", "Пароль должен быть ≥ 8 символов")
        return

    window = name_le.window()
    register_user(name, surname, email, pwd, email_code_users, window)


def register_user(user_name, user_surname, user_email, user_pwd, email_code_users, window) -> None:
    """Регитрация пользователя с введенными данными"""
    user_id = uuid4()
    hash_pwd = hash_password(user_pwd)

    try:
        status, message = create_user_account(user_id, user_name, user_surname, user_email, hash_pwd)
        if status:
            del email_code_users[user_email]

            user_data = {
                "user_name": user_name,
                "user_surname": user_surname,
                "user_email": user_email,
                "hash_password": hash_pwd,
            }

            app_state.all_users_info[str(user_id)] = user_data

            QMessageBox.information(window, "Успешно", message)
            print(f"Словарь пользователей: {app_state.all_users_info}")
            close_reg_or_login_open_car_parameters(app_state.reg_win, user_id)
        else:
            QMessageBox.warning(window, "Ошибка", message)

    except Exception as e:
        QMessageBox.warning(window, "Ошибка отправки", f"Не удалось отправить письмо: {str(e)}")
