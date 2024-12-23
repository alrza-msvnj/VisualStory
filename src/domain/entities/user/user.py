from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from src.domain.entities.base_entity import BaseEntity


class User(BaseEntity):
    __tablename__ = 'users'  # user conflicts with reserved keywords

    username: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    profile_picture_url: Mapped[str] = mapped_column(nullable=True)
    bio: Mapped[str] = mapped_column(nullable=True)
    join_date: Mapped[datetime] = mapped_column(default=datetime.now())
    last_login: Mapped[datetime] = mapped_column(default=datetime.now())
    is_active: Mapped[bool] = mapped_column(nullable=True, default=True)
    role: Mapped[str] = mapped_column(nullable=True, default='user')
