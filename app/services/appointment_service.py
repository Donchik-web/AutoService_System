import os
from PyQt6.QtWidgets import QCalendarWidget, QComboBox, QMessageBox

from database.services.appointment_service import create_note
from database.services.vehicle_repository import create_auto_information
from app.utils.schedule_settings import get_busy_dates


def save_appointment(calendar: QCalendarWidget, time_combo: QComboBox, user_id, auto_data) -> None:
    """Сбор выбранных данных и вывод подтверждения"""
    date_qdate = calendar.selectedDate()
    time = time_combo.currentText()

    busy_dates = get_busy_dates()

    if date_qdate.dayOfWeek() in [6, 7]:
        QMessageBox.warning(calendar.window(), "Ошибка", "Запись в выходные дни невозможна")
        return
    if date_qdate in busy_dates:
        QMessageBox.warning(calendar.window(), "Ошибка", "Запись в выходные дни невозможна")
        return

    from datetime import date
    date_obj = date(date_qdate.year(), date_qdate.month(), date_qdate.day())

    status_note, message_note, user_email = create_note(user_id=user_id, date=date_obj, time=time)

    if status_note is not True:
        QMessageBox.warning(calendar.window(), "Ошибка", message_note)
        return

    status_car, message_car = create_auto_information(user_id=user_id,
                                                      brand=auto_data['auto_brand'], model=auto_data['auto_model'],
                                                      year=auto_data['auto_year'], mileage=auto_data['auto_mileage'])

    if status_car is not True:
        QMessageBox.warning(calendar.window(), "Ошибка", message_car)
        return

    QMessageBox.information(calendar.window(), "Запись подтверждена", message_note)

    from app.services.email_verification_service import connect_smtp_server
    from app.email_messages import messages_to_email

    connect_smtp_server(user_email, str(date_obj) + " " + str(time), messages_to_email, 'confirm_note')

    from app.exports.excel_exporter import filling_excel
    from app.app_state import EXCEL_DIR, FULL_EXCEL_FILE, all_users_info

    if not os.path.exists(EXCEL_DIR):
        os.makedirs(EXCEL_DIR, exist_ok=True)

    filling_excel(FULL_EXCEL_FILE, "Данные", str(user_id), all_users_info, auto_data)

    from app.utils.navigation_manager import close_schedule_open_car_parameters
    close_schedule_open_car_parameters(user_id)