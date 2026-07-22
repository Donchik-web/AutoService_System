from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QTableWidgetItem)

from app.utils.widget_factory import create_label, create_button
from app.utils.vehicle_history_utils import create_cars_table, export_filtered_data


def build_vehicle_history_form(parent: QWidget, user_data: dict, autos_list_from_dict: list) -> None:
    """История автомобилей"""
    main_layout = QVBoxLayout(parent)
    main_layout.setContentsMargins(30, 30, 30, 30)
    main_layout.setSpacing(12)

    title_layout = QHBoxLayout()
    title_label = QLabel("Автопарк пользователя")
    user_label = QLabel(f"{user_data.get('name', '')} {user_data.get('surname', '')}")

    title_layout.addWidget(title_label)
    title_layout.addStretch()
    title_layout.addWidget(user_label)

    table = create_cars_table(autos_list_from_dict)

    filter_layout = QHBoxLayout()

    year_combo = QComboBox()
    year_combo.addItems(["Все года", "После 2020", "2020 и старше"])
    year_combo.setFixedWidth(180)

    mileage_combo = QComboBox()
    mileage_combo.addItems(["Весь пробег", "Больше 100к", "Меньше 100к"])
    mileage_combo.setFixedWidth(180)

    filter_layout.addWidget(create_label("Фильтр:", size=14))
    filter_layout.addWidget(year_combo)
    filter_layout.addWidget(mileage_combo)

    def update_table_with_filters():
        year_filter = year_combo.currentText()
        mileage_filter = mileage_combo.currentText()

        from database.services.vehicle_repository import get_user_cars
        success, message, _, cars = get_user_cars(user_id=user_data['user_id'])

        if success:
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

                filtered_cars.append(car)

            table.setRowCount(len(filtered_cars))
            for row, car in enumerate(filtered_cars):
                table.setItem(row, 0, QTableWidgetItem(car['brand']))
                table.setItem(row, 1, QTableWidgetItem(car['model']))
                table.setItem(row, 2, QTableWidgetItem(str(car['year'])))
                table.setItem(row, 3, QTableWidgetItem(str(car['mileage'])))

    year_combo.currentTextChanged.connect(lambda: update_table_with_filters())
    mileage_combo.currentTextChanged.connect(lambda: update_table_with_filters())

    main_layout.addLayout(title_layout)
    main_layout.addLayout(filter_layout)
    main_layout.addWidget(table)

    button_layout = QHBoxLayout()

    from app.utils.navigation_manager import close_vehicle_repository_open_car_parameters
    close_btn = create_button(text="Закрыть", bg="#e74c3c", hover="#c0392b",
                              callback=close_vehicle_repository_open_car_parameters,
                              user_id=user_data.get('user_id', ''))

    export_btn = create_button(text="Экспорт в Excel", bg="#27ae60", hover="#2ecc71",
                               callback=lambda: export_filtered_data(
                                   user_data.get('user_id', ''),
                                   year_combo.currentText(),
                                   mileage_combo.currentText(),
                                   parent
                               ))

    button_layout.addStretch()
    button_layout.addWidget(export_btn)
    button_layout.addWidget(close_btn)
    main_layout.addLayout(button_layout)
