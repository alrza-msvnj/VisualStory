from src.api.controllers.base_controller import BaseController
from src.application.services.user_service import UserService
from src.application.dtos.user.user import UserResponse


class UserController(BaseController[UserResponse, UserService]):
    def __init__(self):
        super().__init__(UserService())
