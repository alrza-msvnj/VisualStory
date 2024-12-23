from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.domain.entities.user.user import User
from src.domain.entities.user.user_repository import IUserRepository
from src.infrastructure.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User], IUserRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, User)

    async def get_by_username(self, username: str) -> Optional[User]:
        return (await self.db.scalars(select(User).where(User.username == username))).first()

    async def get_by_email(self, email: str) -> Optional[User]:
        return (await self.db.scalars(select(User).where(User.email == email))).first()
