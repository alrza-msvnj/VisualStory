from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.entities.user.user import User
from src.infrastructure.repositories.user_repository import UserRepository
from src.application.contracts.user_service import IUserService
from src.application.dtos.user.add_user_dto import AddUserRequest, AddUserResponse
from src.application.dtos.user.get_user_dto import GetUserRequest, GetUserResponse
from src.application.dtos.user.get_all_user_dto import GetAllUserResponse
from src.application.dtos.user.update_user_dto import UpdateUserRequest, UpdateUserResponse
from src.application.dtos.user.delete_user_dto import DeleteUserRequest, DeleteUserResponse
from src.application.dtos.user.get_by_username_dto import GetByUsernameRequest, GetByUsernameResponse


class UserService(IUserService):
    def __init__(self, db: AsyncSession):
        self.repository = UserRepository(db)

    async def add(self, request: AddUserRequest) -> AddUserResponse:
        user = User(**request.model_dump())
        user = await self.repository.add(user)
        response = AddUserResponse.model_validate(user)
        return response

    async def get(self, request: GetUserRequest) -> GetUserResponse:
        user = await self.repository.get(request.id)
        response = GetUserResponse.model_validate(user)
        return response

    async def get_all(self) -> List[GetAllUserResponse]:
        users = await self.repository.get_all()
        response = [GetAllUserResponse.model_validate(user) for user in users]
        return response

    async def update(self, request: UpdateUserRequest) -> UpdateUserResponse:
        user = User(**request.model_dump())
        user = await self.repository.update(user)
        response = UpdateUserResponse.model_validate(user)
        return response

    async def delete(self, request: DeleteUserRequest) -> DeleteUserResponse:
        response = await self.repository.delete(request.id)
        return DeleteUserResponse(deleted=response)

    async def get_by_username(self, request: GetByUsernameRequest) -> GetByUsernameResponse:
        user = await self.repository.get_by_username(request.username)
        response = GetByUsernameResponse.model_validate(user)
        return response
