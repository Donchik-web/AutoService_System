from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QTableWidget, QHeaderView
from PyQt6.QtGui import QFont

from app.utils.style_manager import line_edit_style, button_style


def create_label(text: str, size: int = 16) -> QLabel:
    """Создание подписей к полям ввода"""
    lbl = QLabel(text)
    weight = QFont.Weight.Bold
    lbl.setFont(QFont("Arial", size, weight))
    return lbl


def create_input(placeholder: str, echo: QLineEdit.EchoMode = QLineEdit.EchoMode.Normal) -> QLineEdit:
    """Поле ввода"""
    le = QLineEdit()
    le.setPlaceholderText(placeholder)
    le.setFixedHeight(65)
    le.setEchoMode(echo) # отображение вводимого текста (для пароля вывод символов)
    le.setStyleSheet(line_edit_style())
    return le


def create_button(text: str, bg: str, hover: str, callback, user_id = None) -> QPushButton:
    """Кнопка с общим оформлением"""
    btn = QPushButton(text)
    btn.setFixedHeight(65)
    btn.setStyleSheet(button_style(bg, hover))
    if user_id is None:
        btn.clicked.connect(callback)
    else:
        btn.clicked.connect(lambda: callback(user_id))

    return btn


def create_table(row_count: int, column_count: int, headers: list[str] = None, header_font_size: int = 16) -> QTableWidget:
    """Создание базовой таблицы с заголовками"""
    table = QTableWidget(row_count, column_count)

    if headers:
        table.setHorizontalHeaderLabels(headers)

    table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    table.verticalHeader().setVisible(False)

    table.setStyleSheet(f"""
        QTableWidget {{
            font-size: 16px;
            gridline-color: #ddd;
        }}
        QHeaderView::section {{
            background-color: #2c3e50;
            color: white;
            padding: 8px;
            font-weight: bold;
            font-size: {header_font_size}px;
        }},
    """)

    return table