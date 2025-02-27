from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.domain.entities.base_entity import BaseEntity
from src.domain.entities.user.user import User


class Post(BaseEntity):
    __tablename__ = 'posts'

    content: Mapped[str] = mapped_column(nullable=False)
    image_url: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(), onupdate=datetime.now())
    
    # Foreign key relationship with User
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    user: Mapped[User] = relationship('User', back_populates='posts')
    
    is_deleted: Mapped[bool] = mapped_column(default=False)
