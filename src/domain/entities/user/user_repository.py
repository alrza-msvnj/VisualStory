from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.base_repository import IBaseRepository
from src.domain.entities.user.user import User


class IUserRepository(IBaseRepository[User], ABC):

    @abstractmethod
    async def get_by_username(self, username: str) -> Optional[User]:
        pass
