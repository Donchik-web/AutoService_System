from PyQt6.QtWidgets import QCalendarWidget
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QTextCharFormat, QColor


def get_busy_dates() -> list[QDate]:
    """Формирует занятые дни"""
    today = QDate.currentDate()
    return [today.addDays(2), today.addDays(5), today.addDays(9)]


def paint_busy_dates(cal: QCalendarWidget) -> None:
    """Занятые даты красит в красный цвет"""
    fmt = QTextCharFormat()
    fmt.setForeground(QColor("red"))
    for d in get_busy_dates():
        cal.setDateTextFormat(d, fmt)