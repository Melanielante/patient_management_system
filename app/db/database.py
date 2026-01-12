from sqlalchemy import create_engine
from app.db.base import Base
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://patient_user:strongpassword@localhost/patient_db"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=True,
)
