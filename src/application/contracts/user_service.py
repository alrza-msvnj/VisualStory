from abc import ABC
from src.application.dtos.user.user import UserRequest, UserResponse
from src.application.contracts.base_service import IBaseService


class IUserService(IBaseService[UserRequest, UserResponse], ABC):
    async def get_by_username(self, username: str) -> UserResponse:
        pass
