from abc import ABC
from src.application.contracts.base_service import IBaseService
from src.application.dtos.user.user import UserResponse


class IUserService(IBaseService[UserResponse], ABC):
    async def get_by_username(self, username: str) -> UserResponse:
        pass
