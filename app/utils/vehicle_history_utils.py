import os

from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget, QMessageBox
from app.utils.widget_factory import create_table
from database.services.vehicle_repository import get_user_cars


def create_cars_table(cars_data: list) -> QTableWidget:
    """Создание таблицы через фабрику и заполнение через цикл"""
    table = create_table(
        row_count=len(cars_data),
        column_count=4,
        headers=["Марка", "Модель", "Год выпуска", "Пробег (км)"],
        header_font_size=17
    )

    for row, car_info in enumerate(cars_data):
        table.setItem(row, 0, QTableWidgetItem(car_info.get("brand", "")))
        table.setItem(row, 1, QTableWidgetItem(car_info.get("model", "")))
        table.setItem(row, 2, QTableWidgetItem(str(car_info.get("year", ""))))
        table.setItem(row, 3, QTableWidgetItem(str(car_info.get("mileage", ""))))

    return table


def export_filtered_data(user_id: str, year_filter: str, mileage_filter: str, window):
    """Экспортирует отфильтрованные данные в Excel"""
    from app.exports.excel_exporter import filling_excel
    from app.app_state import EXCEL_DIR, CRITERIA_EXCEL_FILE, all_users_info

    success, message, _, cars = get_user_cars(user_id=user_id)

    if not success:
        QMessageBox.warning(window, "Ошибка", "Не удалось загрузить данные")
        return

    filtered_cars = []
    for car in cars:
        if year_filter == "После 2020" and car['year'] <= 2020:
            continue
        if year_filter == "2020 и старше" and car['year'] > 2020:
            continue

        if mileage_filter == "Больше 100к" and car['mileage'] <= 100000:
            continue
        if mileage_filter == "Меньше 100к" and car['mileage'] >= 100000:
            continue

        auto_data = {
            'auto_brand': car['brand'],
            'auto_model': car['model'],
            'auto_year': car['year'],
            'auto_mileage': car['mileage']
        }
        filtered_cars.append(auto_data)

    if not filtered_cars:
        QMessageBox.warning(window, "Ошибка", "Нет данных для экспорта")
        return

    if not os.path.exists(EXCEL_DIR):
        os.makedirs(EXCEL_DIR, exist_ok=True)

    if os.path.exists(CRITERIA_EXCEL_FILE):
        os.remove(CRITERIA_EXCEL_FILE)
        print("Удален Excel файл для импорта машин, выбранных через критерии")

    for auto_data in filtered_cars:
        filling_excel(CRITERIA_EXCEL_FILE, "Данные", str(user_id), all_users_info, auto_data)

    QMessageBox.information(window, "Успех", f"Экспортировано {len(filtered_cars)} автомобилей")