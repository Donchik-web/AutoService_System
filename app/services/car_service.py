from PyQt6.QtWidgets import QMessageBox


def processing_car_data(user_id, brand_le, model_le, year_le, mileage_le):
    brand = brand_le.text().strip()
    model = model_le.text().strip()
    year_text = year_le.text().strip()
    mileage_text = mileage_le.text().strip()

    if not brand:
        QMessageBox.warning(brand_le.window(), "Ошибка", "Введите марку автомобиля")
        return
    if not model:
        QMessageBox.warning(model_le.window(), "Ошибка", "Укажите модель автомобиля")
        return

    if not year_text:
        QMessageBox.warning(year_le.window(), "Ошибка", "Необходимо указать год выпуска авто")
        return

    try:
        year = int(year_text)
        if year > 2026:
            QMessageBox.warning(year_le.window(), "Ошибка", "Год выпуска не может быть больше текущего")
            return
        elif year < 1886:
            QMessageBox.warning(year_le.window(), "Ошибка", "Год выпуска не может быть меньше 1886 (год создания первого автомобиля)")
            return
    except ValueError:
            QMessageBox.warning(year_le.window(), "Ошибка", "Год должен быть числом")
            return

    if not mileage_text:
        QMessageBox.warning(mileage_le.window(), "Ошибка", "Необходимо указать пробег автомобиля")
        return
    try:
        mileage = int(mileage_text)
        if mileage < 0:
            QMessageBox.warning(mileage_le.window(), "Ошибка", "Пробег не может быть отрицательным")
            return
        elif mileage > 999999:
            QMessageBox.warning(mileage_le.window(), "Ошибка", "Укажите настоящий пробег")
            return
    except ValueError:
        QMessageBox.warning(mileage_le.window(), "Ошибка", "Пробег должен быть целым числом")
        return

    auto_data = {
        "auto_brand": brand,
        "auto_model": model,
        "auto_year": year,
        "auto_mileage": mileage,
    }

    from app.utils.navigation_manager import close_car_parameters_open_schedule
    close_car_parameters_open_schedule(user_id, auto_data)