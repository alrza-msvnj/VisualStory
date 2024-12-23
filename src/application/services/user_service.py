from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.entities.user.user import User
from src.domain.entities.user.user_repository import IUserRepository
from src.infrastructure.repositories.user_repository import UserRepository
from src.application.dtos.user.user import UserRequest, UserResponse
from src.application.contracts.user_service import IUserService
from src.application.services.base_service import BaseService


class UserService(BaseService[UserRequest, UserResponse, User, IUserRepository], IUserService):
    def __init__(self, db: AsyncSession):
        super().__init__(UserRequest, UserResponse, User, UserRepository(db))

    async def get_by_username(self, username: str) -> UserResponse:
        user = await self.repository.get_by_username(username)
        response = self.response_dto.model_validate(user)
        return response
