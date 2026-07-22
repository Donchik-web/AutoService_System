import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


def get_url_db():
    """URL БД"""
    name = os.getenv("DB_NAME", "AutoService")
    os.makedirs("data", exist_ok=True)

    return f"sqlite:///data/{name}.db"


engine = create_engine(get_url_db(), connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)