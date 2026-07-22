import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QFont

from app import app_state
from app.ui.registration_view import build_registration_form


def main() -> None:
    app = QApplication(sys.argv)
    app.setFont(QFont("Arial", 16))

    win = QMainWindow()
    win.setWindowTitle("Регистрация")
    win.setFixedSize(560, 750)

    central = QWidget()
    win.setCentralWidget(central)
    build_registration_form(central)

    app_state.reg_win = win

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
