import os
from sqlalchemy import create_engine, inspect
from database.tables import Base

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(DATA_DIR, exist_ok=True)

db_path = os.path.join(DATA_DIR, 'AutoService.db')


def init_database():
    engine = create_engine(f'sqlite:///{db_path}', connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)

    return engine


if __name__ == "__main__":
    init_database()