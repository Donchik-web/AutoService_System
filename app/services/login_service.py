from PyQt6.QtWidgets import QMessageBox, QLineEdit

from app import app_state
from database.services.login_service import login_user, get_user_by_id
from app.utils.navigation_manager import close_reg_or_login_open_car_parameters


def process_login(email_le: QLineEdit, pwd_le: QLineEdit):
    email = email_le.text().strip()
    pwd = pwd_le.text()

    if not email or not pwd:
        QMessageBox.warning(email_le.window(), "Ошибка", "Заполните оба поля")
        return

    status, message, user_id = login_user(email, pwd)

    if status:
        QMessageBox.information(email_le.window(),"Успех", message)

        user_id_str = str(user_id)

        if user_id_str not in app_state.all_users_info:
            status, user_data = get_user_by_id(user_id)
            if status:
                app_state.all_users_info[user_id_str] = user_data
                print(f"Словарь пользователей: {app_state.all_users_info}")
            else:
                print(user_data)

        close_reg_or_login_open_car_parameters(app_state.login_win, user_id)
    else:
        QMessageBox.warning(email_le.window(), "Ошибка", message)
        pwd_le.clear()