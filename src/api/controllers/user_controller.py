from src.api.controllers.base_controller import BaseController
from src.application.services.user_service import UserService
from src.application.dtos.user.user import UserResponse


class UserController(BaseController[UserResponse, UserService]):
    def __init__(self):
        super().__init__(UserService())

        self.router.get("/get_by_username/{username}", response_model=UserResponse)(self.get_by_username)

    async def get_by_username(self, username: str) -> UserResponse:
        user = await self.service.get_by_username(username)

        return user
