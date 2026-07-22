from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy)

from app.utils.widget_factory import create_input, create_label, create_button
from app.app_state import email_confirmation_code_users
from app.services.email_verification_service import submission_push_code
from app.services.user_registration_service import processing_registration_data
from app.utils.navigation_manager import close_reg_and_open_login


def build_registration_form(parent: QWidget) -> None:
    """Форма регистрации"""
    main_layout = QVBoxLayout(parent)
    main_layout.setContentsMargins(30, 30, 30, 30)

    title = QLabel("Автосервис Северный")
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title.setFont(QFont("Arial", 30, QFont.Weight.Bold))
    title.setStyleSheet("color:#46bbbd;margin-bottom:10px;")
    main_layout.addWidget(title)

    name_surname_hbox = QHBoxLayout()

    name_vbox = QVBoxLayout()
    name_label = create_label("Имя *")
    name_input = create_input("Ваше имя")
    name_vbox.addWidget(name_label)
    name_vbox.addWidget(name_input)
    name_surname_hbox.addLayout(name_vbox)


    surname_vbox = QVBoxLayout()
    surname_label = create_label("Фамилия *")
    surname_input = create_input("Ваша фамилия")
    surname_vbox.addWidget(surname_label)
    surname_vbox.addWidget(surname_input)
    name_surname_hbox.addLayout(surname_vbox)
    main_layout.addLayout(name_surname_hbox)

    email_vbox = QVBoxLayout()
    email_label = create_label("Email *")
    email_input = create_input("example@mail.com")
    email_vbox.addWidget(email_label)
    email_vbox.addWidget(email_input)
    main_layout.addLayout(email_vbox)

    code_vbox = QVBoxLayout()
    code_label = create_label("Код подтверждения *")
    code_hbox = QHBoxLayout()

    code_input = create_input("Введите код из письма")
    send_code_btn = create_button(text="Отправить код", bg="#3498db", hover="#2980b9",
        callback=lambda: submission_push_code(email_input, send_code_btn, email_confirmation_code_users)
    )
    send_code_btn.setFixedWidth(120)

    code_hbox.addWidget(code_input)
    code_hbox.addWidget(send_code_btn)
    code_vbox.addWidget(code_label)
    code_vbox.addLayout(code_hbox)
    main_layout.addLayout(code_vbox)

    pwd_vbox = QVBoxLayout()
    pwd_label = create_label("Пароль *")
    pwd_input = create_input(placeholder="Минимум 8 символов", echo=QLineEdit.EchoMode.Password)
    pwd_vbox.addWidget(pwd_label)
    pwd_vbox.addWidget(pwd_input)
    main_layout.addLayout(pwd_vbox)

    register_btn = create_button(text="ЗАРЕГИСТРИРОВАТЬСЯ", bg="#27ae60", hover="#219a52",
        callback=lambda: processing_registration_data(name_input, surname_input, email_input, code_input, pwd_input, email_confirmation_code_users)
    )
    register_btn.setSizePolicy(
        QSizePolicy.Policy.Expanding,
        QSizePolicy.Policy.Fixed
    )
    main_layout.addWidget(register_btn)

    # ссылка «Войти»
    login_hbox = QHBoxLayout()
    login_hbox.addStretch()
    login_hint = QLabel("Уже есть аккаунт?")
    login_hint.setStyleSheet("color:#7f8c8d;font-size:16px;")
    login_btn = QPushButton("Войти")
    login_btn.setStyleSheet("""
        QPushButton {
            color:#3498db;
            border:none;
            font-weight:bold;
            font-size:16px;
        }
        QPushButton:hover {
            color:#2980b9;
        }
    """)

    # Связываем кнопку с функцией
    login_btn.clicked.connect(close_reg_and_open_login)
    login_hbox.addWidget(login_hint)
    login_hbox.addWidget(login_btn)
    login_hbox.addStretch()
    main_layout.addLayout(login_hbox)