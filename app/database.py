from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Correctly encoded password
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:Bij1%40endra@localhost:54329/studentdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

