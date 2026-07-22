from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from app.utils.widget_factory import create_label, create_input
from app.services.car_registration_service import processing_car_data


def build_car_parameters_form(parent: QWidget, user_id) -> None:
    """Форма ввода марки, модели, года выпуска и пробега."""
    layout = QVBoxLayout(parent)
    layout.setContentsMargins(30, 30, 30, 30)
    layout.setSpacing(12)

    title = QLabel("ИНФОРМАЦИЯ ОБ АВТОМОБИЛЕ")
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
    title.setStyleSheet("color:#46bbbd;margin-bottom:20px;")
    layout.addWidget(title)

    brand_box = QVBoxLayout()
    brand_box.addWidget(create_label("Марка *"))
    brand_input = create_input("Toyota, BMW, …")
    brand_box.addWidget(brand_input)
    layout.addLayout(brand_box)

    model_box = QVBoxLayout()
    model_box.addWidget(create_label("Модель *"))
    model_input = create_input("Camry, X5, …")
    model_box.addWidget(model_input)
    layout.addLayout(model_box)

    year_box = QVBoxLayout()
    year_box.addWidget(create_label("Год выпуска *"))
    year_input = create_input("2005")
    year_box.addWidget(year_input)
    layout.addLayout(year_box)

    mileage_box = QVBoxLayout()
    mileage_box.addWidget(create_label("Пробег (км) *"))
    mileage_input = create_input("120000")
    mileage_box.addWidget(mileage_input)
    layout.addLayout(mileage_box)

    from app.utils.widget_factory import create_button
    from app.utils.navigation_manager import close_car_parameters_open_vehicle_repository, close_car_parameters_and_exit_to_login

    back_btn = create_button(text="Назад", bg="#95a5a6", hover="#7f8c8d", callback=close_car_parameters_and_exit_to_login,  user_id=user_id)

    history_btn = create_button(text="История моих автомобилей", bg='#9b59b6', hover='#008B8B', callback=lambda: close_car_parameters_open_vehicle_repository(str(user_id)))

    next_btn = create_button(text="ДАЛЕЕ", bg="#27ae60", hover="#219a52", callback=lambda: processing_car_data(user_id, brand_input, model_input, year_input, mileage_input))

    layout.addWidget(back_btn)
    layout.addWidget(history_btn)
    layout.addWidget(next_btn)