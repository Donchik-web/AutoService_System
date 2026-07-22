from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QSizePolicy, QCalendarWidget, QComboBox, QHBoxLayout)

from app.utils.widget_factory import create_label, create_button
from app.utils.schedule_settings import paint_busy_dates
from app.services.appointment_service import save_appointment


def build_schedule_form(parent: QWidget, user_id, auto_data) -> None:
    """Создаёт форму выбора даты и времени"""
    layout = QVBoxLayout(parent)
    layout.setContentsMargins(30, 30, 30, 30)
    layout.setSpacing(12)

    title = QLabel("ВЫБОР ДАТЫ И ВРЕМЕНИ")
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title.setFont(QFont("Arial", 26, QFont.Weight.Bold))
    title.setStyleSheet("color:#46bbbd;margin-bottom:20px;")
    layout.addWidget(title)

    layout.addWidget(create_label("Дата записи *"))
    calendar = QCalendarWidget()
    calendar.setGridVisible(True)
    calendar.setMinimumDate(QDate.currentDate())
    paint_busy_dates(calendar)
    layout.addWidget(calendar)

    layout.addWidget(create_label("Время *"))
    time_combo = QComboBox()
    for hour in range(9, 21):
        time_combo.addItem(f"{hour:02d}:00")
    layout.addWidget(time_combo)

    save_btn = create_button(text="СОХРАНИТЬ", bg="#27ae60", hover="#219a52", callback=lambda: save_appointment(calendar, time_combo, user_id, auto_data))
    save_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
    layout.addWidget(save_btn)

    top_buttons_layout = QHBoxLayout()
    top_buttons_layout.addStretch()

    from app.utils.navigation_manager import close_schedule_open_car_parameters
    back_btn = create_button(text="Назад", bg="#95a5a6", hover="#7f8c8d", callback=close_schedule_open_car_parameters, user_id=user_id)
    top_buttons_layout.addWidget(back_btn, stretch=1)

    layout.addLayout(top_buttons_layout)