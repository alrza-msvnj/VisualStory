from abc import ABC, abstractmethod
from typing import List
from src.application.dtos.user.add_user_dto import AddUserRequest, AddUserResponse
from src.application.dtos.user.get_user_dto import GetUserRequest, GetUserResponse
from src.application.dtos.user.get_all_user_dto import GetAllUserResponse
from src.application.dtos.user.update_user_dto import UpdateUserRequest, UpdateUserResponse
from src.application.dtos.user.delete_user_dto import DeleteUserRequest, DeleteUserResponse
from src.application.dtos.user.get_by_username_dto import GetByUsernameRequest, GetByUsernameResponse


class IUserService(ABC):

    @abstractmethod
    async def add(self, request: AddUserRequest) -> AddUserResponse:
        pass

    @abstractmethod
    async def get(self, request: GetUserRequest) -> GetUserResponse:
        pass

    @abstractmethod
    async def get_all(self) -> List[GetAllUserResponse]:
        pass

    @abstractmethod
    async def update(self, request: UpdateUserRequest) -> UpdateUserResponse:
        pass

    @abstractmethod
    async def delete(self, request: DeleteUserRequest) -> DeleteUserResponse:
        pass

    @abstractmethod
    async def get_by_username(self, request: GetByUsernameRequest) -> GetByUsernameResponse:
        pass
