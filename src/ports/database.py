from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'postgresql+psycopg2://username:password@localhost:5432/visualstory'

engine = create_engine(DATABASE_URL, echo=True)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
