import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@db:5432/proyectosdb")
print(f"📌 DATABASE_URL usada por SQLAlchemy: {DATABASE_URL}")  # Depuración

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()  # ✅ Uso correcto en SQLAlchemy 2.0
