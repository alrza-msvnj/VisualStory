from sqlalchemy import Column, Integer
from src.infrastructure.database import Base


class BaseEntity(Base):
    __abstract__ = True  # prevents creating a table or instantiating an object for this class

    id = Column(Integer, primary_key=True, autoincrement=True)
