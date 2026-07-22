import os

from typing import Optional
from PyQt6.QtWidgets import QMainWindow

# Основные окна программы
reg_win: Optional[QMainWindow] = None
login_win: Optional[QMainWindow] = None
car_win: Optional[QMainWindow] = None
schedule_win: Optional[QMainWindow] = None
vehicle_history_win: Optional[QMainWindow] = None

# Словарь для работы с email кодом подтверждения
email_confirmation_code_users = {}

# Общий список клиентов для JSON
all_users_info = {}

# Файлы по экспорту
EXPORT_DIR = "app/exports"
EXCEL_DIR = os.path.join(EXPORT_DIR, "excel")

# Файлы
FULL_EXCEL_FILE = os.path.join(EXCEL_DIR, "Все_автомобили_клиентов.xlsx")
CRITERIA_EXCEL_FILE = os.path.join(EXCEL_DIR, "Автомобили_клиента_по_критериям.xlsx")