from sqlalchemy import Column, String
from dataclasses import dataclass
from typing import Optional
from base_entity import BaseEntity

@dataclass
class User(BaseEntity):
    __tablename__ = 'users' # user conflicts with reserved keywords

    username: str = Column(String, unique=True, nullable=False)
    email: str = Column(String, unique=True, nullable=False)
    bio: Optional[str] = Column(String, nullable=True)
    profile_image_url: Optional[str] = Column(String, nullable=True)