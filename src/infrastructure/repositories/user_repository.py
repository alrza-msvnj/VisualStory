from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.future import select
from typing import Optional
from src.domain.entities.user.user_repository import IUserRepository
from src.infrastructure.base_repository import BaseRepository
from src.domain.entities.user.user import User


class UserRepository(BaseRepository[User], IUserRepository):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        super().__init__(session_factory, User)

    async def get_by_username(self, username: str) -> Optional[User]:
        async with self.session_factory() as db:
            user = await db.execute(select(User).filter_by(username=username))
            user = user.scalars().first()

            return user

    async def get_by_email(self, email: str) -> Optional[User]:
        async with self.session_factory() as db:
            user = await db.execute(select(User).filter_by(email=email))
            user = user.scalars().first()

            return user
