from database.connection import Session
from database.tables import Notes, Users
from datetime import datetime, timezone
from uuid import uuid4


def create_note(user_id, date, time):
    try:
        with Session() as session:
            from datetime import datetime as dt
            time_obj = dt.strptime(time, "%H:%M").time()

            existing_note = session.query(Notes).filter(
                Notes.date == date,
                Notes.time == time_obj
            ).first()

            if existing_note:
                return None, f"Это время уже занято. Выберите другую дату или время", None

            if hasattr(user_id, 'hex'):  # если это UUID объект
                user_id = str(user_id)

            note = Notes(
                id=str(uuid4()),  # Преобразуем UUID в строку
                user_id=user_id,
                date=date,
                time=time_obj,
                created_at=datetime.now(timezone.utc)
            )

            session.add(note)
            session.commit()

            user_email_for_msg = session.query(Users.email).filter(Users.id == user_id).scalar()
            return True, f"Вы записаны на {date} в {time}", user_email_for_msg
    except Exception as e:
        return None, f"Общая ошибка: {e}", None