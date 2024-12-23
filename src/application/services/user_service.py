from sqlalchemy.ext.asyncio import AsyncSession
from src.application.contracts.user_service import IUserService
from src.application.dtos.user.user import UserResponse
from src.application.services.base_service import BaseService
from src.domain.entities.user.user import User
from src.domain.entities.user.user_repository import IUserRepository
from src.infrastructure.repositories.user_repository import UserRepository


class UserService(BaseService[UserResponse, User, IUserRepository], IUserService):
    def __init__(self, db: AsyncSession):
        super().__init__(UserResponse, User, UserRepository(db))

    async def get_by_username(self, username: str) -> UserResponse:
        user = await self.repository.get_by_username(username)
        response = self.response_dto.model_validate(user)

        return response
