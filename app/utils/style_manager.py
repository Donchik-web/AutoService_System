def line_edit_style() -> str:
    """Стиль для полей ввода"""
    return """
        QLineEdit {
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            padding: 0 12px;
            font-size: 20px;
        }
        QLineEdit:focus {
            border-color: #3498db;
        }
    """


def button_style(bg: str, hover: str) -> str:
    """Стиль для кнопок"""
    return f"""
        QPushButton {{
            background-color: {bg};
            color: white;
            border-radius: 10px;
            font-weight: bold;
            font-size: 15px;
        }}
        QPushButton:hover {{ background-color: {hover}; }}
        QPushButton:pressed {{
            background-color: {bg};
        }}
    """
