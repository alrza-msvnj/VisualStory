from src.application.contracts.user_service import IUserService
from src.application.dtos.user.user import UserResponse
from src.application.services.base_service import BaseService
from src.domain.entities.user.user import User
from src.infrastructure.database import session_factory
from src.infrastructure.repositories.user_repository import UserRepository


class UserService(BaseService[UserResponse, User, UserRepository], IUserService):
    def __init__(self):
        super().__init__(UserResponse, User, UserRepository(session_factory))

    async def get_by_username(self, username: str) -> User:
        user = await self.repository.get_by_username(username)
        response = self.response_dto.model_validate(user)

        return response
