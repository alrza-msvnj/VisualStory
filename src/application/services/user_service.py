import os.path
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
from src.application.dtos.user.get_profile_picture_dto import GetProfilePictureRequest, GetProfilePictureResponse
from src.application.dtos.user.save_profile_picture_dto import SaveProfilePictureRequest, SaveProfilePictureResponse


class UserService(IUserService):
    def __init__(self, db: AsyncSession):
        self.user_repository = UserRepository(db)

    async def add(self, request: AddUserRequest) -> AddUserResponse:
        user = User(**request.model_dump())
        user = await self.user_repository.add(user)
        response = AddUserResponse.model_validate(user)
        return response

    async def get(self, request: GetUserRequest) -> GetUserResponse:
        user = await self.user_repository.get(request.id)
        response = GetUserResponse.model_validate(user)
        return response

    async def get_all(self) -> List[GetAllUserResponse]:
        users = await self.user_repository.get_all()
        response = [GetAllUserResponse.model_validate(user) for user in users]
        return response

    async def update(self, request: UpdateUserRequest) -> UpdateUserResponse:
        user = User(**request.model_dump())
        user = await self.user_repository.update(user)
        response = UpdateUserResponse.model_validate(user)
        return response

    async def delete(self, request: DeleteUserRequest) -> DeleteUserResponse:
        response = await self.user_repository.delete(request.id)
        return DeleteUserResponse(deleted=response)

    async def get_by_username(self, request: GetByUsernameRequest) -> GetByUsernameResponse:
        user = await self.user_repository.get_by_username(request.username)
        response = GetByUsernameResponse.model_validate(user)
        return response

    async def get_profile_picture(self, request: GetProfilePictureRequest) -> GetProfilePictureResponse:
        user = await self.user_repository.get(request.user_id)

        response = GetProfilePictureResponse(
            profile_picture=str(user.profile_picture)
        )

        if user.profile_picture:
            file_path = os.path.join('src/ui/static/assets/profile_pictures', str(user.profile_picture))
            if not os.path.exists(file_path):
                response.profile_picture = None

        return response

    async def save_profile_picture(self, request: SaveProfilePictureRequest) -> SaveProfilePictureResponse:
        user = await self.user_repository.get(request.user_id)

        if user.profile_picture:
            file_path = os.path.join('src/ui/static/assets/profile_pictures', str(user.profile_picture))
            if os.path.exists(file_path):
                os.remove(file_path)

        user.profile_picture = request.profile_picture
        await self.user_repository.update(user)
        response = SaveProfilePictureResponse(
            success=True
        )
        return response
