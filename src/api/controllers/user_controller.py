from typing import List
from fastapi import Depends, APIRouter
from src.application.contracts.user_service import IUserService
from src.application.dependencies import get_user_service
from src.application.dtos.user.add_user_dto import AddUserRequest, AddUserResponse
from src.application.dtos.user.get_user_dto import GetUserRequest, GetUserResponse
from src.application.dtos.user.get_all_user_dto import GetAllUserResponse
from src.application.dtos.user.update_user_dto import UpdateUserRequest, UpdateUserResponse
from src.application.dtos.user.delete_user_dto import DeleteUserRequest, DeleteUserResponse
from src.application.dtos.user.get_by_username_dto import GetByUsernameRequest, GetByUsernameResponse


class UserController:
    def __init__(self):
        self.router = APIRouter(prefix="/api/user", tags=["User"])
        self.router.post("/", response_model=AddUserResponse)(self.add)
        self.router.get("/{id}", response_model=GetUserResponse)(self.get)
        self.router.get("/", response_model=List[GetAllUserResponse])(self.get_all)
        self.router.put("/", response_model=UpdateUserResponse)(self.update)
        self.router.delete("/{id}")(self.delete)
        self.router.get("/get_by_username/{username}", response_model=GetByUsernameResponse)(self.get_by_username)

    @staticmethod
    async def add(user: AddUserRequest, service: IUserService = Depends(get_user_service)) -> AddUserResponse:
        return await service.add(user)

    @staticmethod
    async def get(user_id: int, service: IUserService = Depends(get_user_service)) -> GetUserResponse:
        return await service.get(GetUserRequest(id=user_id))

    @staticmethod
    async def get_all(service: IUserService = Depends(get_user_service)) -> List[GetAllUserResponse]:
        return await service.get_all()

    @staticmethod
    async def update(entity: UpdateUserRequest, service: IUserService = Depends(get_user_service)) -> UpdateUserResponse:
        return await service.update(entity)

    @staticmethod
    async def delete(entity_id: int, service: IUserService = Depends(get_user_service)) -> DeleteUserResponse:
        return await service.delete(DeleteUserRequest(id=entity_id))

    @staticmethod
    async def get_by_username(username: str, user_service: IUserService = Depends(get_user_service)) -> AddUserResponse:
        return await user_service.get_by_username(GetByUsernameRequest(username=username))
