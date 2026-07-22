from PyQt6.QtWidgets import QMainWindow, QWidget
from app import app_state


def close_reg_and_open_login():
    """Закрывает окно регистрации и открывает окно входа"""
    if app_state.reg_win is not None:
        app_state.reg_win.hide()

    open_login_window()


def open_login_window():
    """Создаёт и показывает отдельное окно «Вход»"""
    from app.ui.login_view import build_login_form

    if app_state.login_win is not None:
        app_state.login_win.show()
        app_state.login_win.raise_()
        app_state.login_win.activateWindow()
        return

    win = QMainWindow()
    win.setWindowTitle("Вход")
    win.setFixedSize(560, 750)

    central = QWidget()
    win.setCentralWidget(central)
    build_login_form(central)

    app_state.login_win = win
    win.show()


def close_login_and_open_reg():
    """Закрывает окно входа и открывает окно регистрации"""
    if app_state.login_win is not None:
        app_state.login_win.hide()

    open_registration_window()


def open_registration_window() -> None:
    """Создаёт и показывает отдельное окно «Регистрация»"""
    from app.ui.registration_view import build_registration_form

    if app_state.reg_win is not None:
        app_state.reg_win.show()
        app_state.reg_win.raise_()
        app_state.reg_win.activateWindow()
        return

    win = QMainWindow()
    win.setWindowTitle("Регистрация")
    win.setFixedSize(560, 750)

    central = QWidget()
    win.setCentralWidget(central)
    build_registration_form(central)

    app_state.reg_win = win
    win.show()


def close_reg_or_login_open_car_parameters(win, user_id):
    """Закрывает окно регистрации или входа и открывает окно ввода информации об авто"""
    if win is not None:
        win.hide()

    open_car_parameters_window(user_id)


def open_car_parameters_window(user_id) -> None:
    """Открывает окно «Параметры автомобиля»"""
    from app.ui.car_form_view import build_car_parameters_form

    if app_state.car_win is not None:
        app_state.car_win.show()
        app_state.car_win.raise_()
        app_state.car_win.activateWindow()

    win = QMainWindow()
    win.setWindowTitle("Параметры автомобиля")
    win.setFixedSize(560, 750)

    central = QWidget()
    win.setCentralWidget(central)
    build_car_parameters_form(central, user_id)

    app_state.car_win = win
    win.show()


def close_car_parameters_open_schedule(user_id, auto_data):
    """Закрывает окно параметров авто и открывает окно выбора даты и времени записи"""
    if app_state.car_win is not None:
        app_state.car_win.hide()

    open_schedule_window(user_id, auto_data)


def open_schedule_window(user_id, auto_data) -> None:
    """Создаёт окно «Выбор даты и времени»"""
    from app.ui.schedule_view import build_schedule_form

    if app_state.schedule_win is not None:
        app_state.schedule_win.show()
        app_state.schedule_win.raise_()
        app_state.schedule_win.activateWindow()

    win = QMainWindow()
    win.setWindowTitle("Выбор даты и времени")
    win.setFixedSize(560, 750)

    central = QWidget()
    win.setCentralWidget(central)
    build_schedule_form(central, user_id, auto_data)

    app_state.schedule_win = win
    win.show()


def close_schedule_open_car_parameters(user_id):
    """Закрывает окно выбора даты и времени записи, открывает параметры авто"""
    if app_state.schedule_win is not None:
        app_state.schedule_win.hide()

    open_car_parameters_window(user_id)


def close_car_parameters_open_vehicle_repository(user_id):
    """Закрывает окно параметров авто, открывает информацию об автопарке"""
    if app_state.car_win is not None:
        app_state.car_win.hide()

    from database.services.vehicle_repository import get_user_cars
    success, message, user_data, cars_list = get_user_cars(user_id, sort_field='brand', sort_order='asc')

    if success:
        open_vehicle_repository_window(user_data, cars_list)
    else:
        print(f"Не удалось открыть автопарк: {message}")


def open_vehicle_repository_window(user_data, autos_list_from_dict) -> None:
    """Создаёт окно «Автопарк пользователя с сортировкой»"""
    from app.ui.vehicle_history_view import build_vehicle_history_form

    if app_state.vehicle_history_win is not None:
        app_state.vehicle_history_win.show()
        app_state.vehicle_history_win.raise_()
        app_state.vehicle_history_win.activateWindow()

    win = QMainWindow()
    win.setWindowTitle("История автомобилей")
    win.setFixedSize(560, 750)

    central = QWidget()
    win.setCentralWidget(central)
    build_vehicle_history_form(central, user_data, autos_list_from_dict)

    app_state.vehicle_history_win = win
    win.show()


def close_vehicle_repository_open_car_parameters(user_id):
    """Закрывает окно автопарка, открывает параметры авто"""
    if app_state.vehicle_history_win is not None:
        app_state.vehicle_history_win.hide()

    open_car_parameters_window(user_id)


def close_car_parameters_and_exit_to_login(user_id):
    """Закрывает окно параметров авто, сбрасывает ID и открывает вход"""
    if app_state.car_win is not None:
        app_state.car_win.hide()

    user_id_str = str(user_id)
    if user_id_str in app_state.all_users_info:
        del app_state.all_users_info[user_id_str]

    open_login_window()
    print(f"Возврат на окно входа (пользователь вышел)")