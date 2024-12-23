from typing import Annotated, List
from fastapi import Depends, APIRouter, status
from src.application.contracts.user_service import IUserService
from src.application.dependencies import get_user_service
from src.application.dtos.user.user import UserResponse, UserRequest


class UserController:
    def __init__(self):
        self.router = APIRouter(prefix="/api/user", tags=["User"])
        self.router.post("/", response_model=UserResponse)(self.add)
        self.router.get("/{id}", response_model=UserResponse)(self.get)
        self.router.get("/", response_model=List[UserResponse])(self.get_all)
        self.router.put("/{id}", response_model=UserResponse)(self.update)
        self.router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)(self.delete)
        self.router.get("/get_by_username/{username}", response_model=UserResponse)(self.get_by_username)

    @staticmethod
    async def add(entity: UserRequest, service: Annotated[IUserService, Depends(get_user_service)]) -> UserResponse:
        return await service.add(entity)

    @staticmethod
    async def get(entity_id: int, service: Annotated[IUserService, Depends(get_user_service)]) -> UserResponse:
        return await service.get(entity_id)

    @staticmethod
    async def get_all(service: Annotated[IUserService, Depends(get_user_service)]) -> List[UserResponse]:
        return await service.get_all()

    @staticmethod
    async def update(entity: UserRequest, service: Annotated[IUserService, Depends(get_user_service)]) -> UserResponse:
        return await service.update(entity)

    @staticmethod
    async def delete(entity_id: int, service: Annotated[IUserService, Depends(get_user_service)]) -> None:
        await service.delete(entity_id)

    @staticmethod
    async def get_by_username(username: str,
                              user_service: Annotated[IUserService, Depends(get_user_service)]) -> UserResponse:
        return await user_service.get_by_username(username)
