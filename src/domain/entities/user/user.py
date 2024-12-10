from sqlalchemy import Column, String, Boolean
from src.domain.entities.base_entity import BaseEntity


class User(BaseEntity):
    __tablename__ = 'users'  # user conflicts with reserved keywords

    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    profile_picture_url = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    join_date = Column(String, nullable=True)
    last_login = Column(String, nullable=True)
    is_active = Column(Boolean, nullable=True)
    role = Column(String, nullable=True)
