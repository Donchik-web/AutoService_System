from database.connection import Session
from database.tables import AutoInformation, Users
from uuid import uuid4


def create_auto_information(user_id, brand, model, year, mileage):
    """Запись в БД с информацией об авто"""
    try:
        with Session() as session:
            print(f"Момент передачи в БД - брэнд: {brand}, модель: {model}, год: {year}, пробег: {mileage}")

            if hasattr(user_id, 'hex'):
                user_id = str(user_id)

            auto = AutoInformation(
                id=str(uuid4()),  # Преобразуем UUID в строку
                user_id=user_id,
                brand=brand,
                model=model,
                year=year,
                mileage=mileage
            )

            session.add(auto)
            session.commit()
            return True, "Информация об автомобиле занесена в БД!"
    except Exception as e:
        return None, f"Общая ошибка: {e}"


def get_sort_condition(sort_field='brand', sort_order='asc'):
    """Условия сортировки выдает"""
    sort_mapping = {
        'brand_asc': AutoInformation.brand.asc(),
        'brand_desc': AutoInformation.brand.desc(),
        'year_asc': AutoInformation.year.asc(),
        'year_desc': AutoInformation.year.desc(),
        'mileage_asc': AutoInformation.mileage.asc(),
        'mileage_desc': AutoInformation.mileage.desc()
    }

    key = f"{sort_field}_{sort_order}"

    return sort_mapping.get(key, AutoInformation.brand.asc())


def get_user_cars(user_id, sort_field='brand', sort_order='asc'):
    """Поиск пользователя и его автопарка с применением сортировки по критериям"""
    try:
        with Session() as session:
            if hasattr(user_id, 'hex'):
                user_id = str(user_id)
            else:
                user_id = str(user_id)

            user = session.query(Users).filter(Users.id == user_id).first()
            if not user:
                return False, "Пользователь не найден", {}, []

            user_data = {
                "user_id": user_id,
                "name": user.name,
                "surname": user.surname,
            }

            sort_condition = get_sort_condition(sort_field, sort_order)

            autos_list = session.query(
                AutoInformation.brand,
                AutoInformation.model,
                AutoInformation.year,
                AutoInformation.mileage
            ).filter(
                AutoInformation.user_id == user_id
            ).order_by(sort_condition).all()

            if not autos_list:
                return True, "Автопарк пуст", user_data, []

            autos_list_from_dict = []
            for auto_info in autos_list:
                car_data = {
                    'brand': auto_info[0],
                    'model': auto_info[1],
                    'year': auto_info[2],
                    'mileage': auto_info[3]
                }
                autos_list_from_dict.append(car_data)

            return True, "Успешно", user_data, autos_list_from_dict

    except Exception as e:
        return False, f"Неожиданная ошибка {e}", {}, []