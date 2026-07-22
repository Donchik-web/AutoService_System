from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QPushButton, QLineEdit)

from app.utils.navigation_manager import close_login_and_open_reg
from app.utils.widget_factory import create_input, create_label, create_button
from app.services.login_service import process_login


def build_login_form(parent: QWidget) -> None:
    """Окно входа"""
    layout = QVBoxLayout(parent)
    layout.setContentsMargins(30, 30, 30, 30)
    layout.setSpacing(15) # небольшие интервалы между блоками

    title = QLabel("ВХОД")
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title.setFont(QFont("Arial", 30, QFont.Weight.Bold))
    title.setStyleSheet("color:#46bbbd;margin-bottom:10px;")
    layout.addWidget(title)

    description = QLabel(
        "Добро пожаловать в «Автосервис Северный»! "
        "Здесь вы можете осуществить запись в автосервис.")
    description.setWordWrap(True)
    description.setAlignment(Qt.AlignmentFlag.AlignCenter)
    description.setStyleSheet("color:#2c3e50;font-size:16px;margin-bottom:20px;")
    layout.addWidget(description)

    benefits = [
        "🛠️ Квалифицированные мастера",
        "🚗 Оригинальные запчасти",
        "📅 Онлайн‑запись 24/7",
        "💳 Система скидок для постоянных клиентов"
    ]
    for line in benefits:
        lbl = QLabel(f"➡️ {line}")
        lbl.setStyleSheet("color:#2c3e50;font-size:16px;")
        lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(lbl)

    email_vbox = QVBoxLayout()
    email_vbox.addWidget(create_label("Email *"))
    email_input = create_input("example@mail.com")
    email_vbox.addWidget(email_input)
    layout.addLayout(email_vbox)

    pwd_vbox = QVBoxLayout()
    pwd_vbox.addWidget(create_label("Пароль *"))
    pwd_input = create_input(
        placeholder="Введите пароль",
        echo=QLineEdit.EchoMode.Password
    )
    pwd_vbox.addWidget(pwd_input)
    layout.addLayout(pwd_vbox)

    login_btn = create_button(text="ВОЙТИ", bg="#3498db", hover="#2980b9", callback=lambda: process_login(email_input, pwd_input))
    login_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
    layout.addWidget(login_btn)

    reg_hbox = QHBoxLayout()
    reg_hbox.addStretch()
    reg_hint = QLabel("Нет аккаунта?")
    reg_hint.setStyleSheet("color:#7f8c8d;font-size:16px;")
    reg_btn = QPushButton("Регистрация")
    reg_btn.setStyleSheet("""
        QPushButton {
            color:#27ae60;
            border:none;
            font-weight:bold;
            font-size:16px;
        }
        QPushButton:hover { 
            color:#219a52; 
        }
    """)

    reg_btn.clicked.connect(close_login_and_open_reg)
    reg_hbox.addWidget(reg_hint)
    reg_hbox.addWidget(reg_btn)
    reg_hbox.addStretch()
    layout.addLayout(reg_hbox)