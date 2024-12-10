from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()

class BaseEntity(Base):
    __bastract__ = True # Prevents creating a table for this class

    id: int = Column(Integer, primary_key=True, autoincrement=True)