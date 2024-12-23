from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()


class BaseEntity(Base):
    __abstract__ = True  # prevents creating a table or instantiating an object for this class

    id = Column(Integer, primary_key=True, autoincrement=True)
