from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional
from src.domain.entities.user.user_repository import IUserRepository
from src.infrastructure.base_repository import BaseRepository
from src.domain.entities.user.user import User


class UserRepository(BaseRepository[User], IUserRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, User)

    async def get_by_username(self, username: str) -> Optional[User]:
        user = await self.db.execute(select(User).filter_by(username=username))
        user = user.scalars().first()

        return user

    async def get_by_email(self, email: str) -> Optional[User]:
        user = await self.db.execute(select(User).filter_by(email=email))
        user = user.scalars().first()

        return user
