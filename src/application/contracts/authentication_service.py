from abc import ABC, abstractmethod
from src.application.dtos.authentication.register_dto import RegisterRequest, RegisterResponse
from src.application.dtos.authentication.login_dto import LoginRequest, LoginResponse
from src.application.dtos.authentication.logout_dto import LogoutRequest, LogoutResponse


class IAuthenticationService(ABC):

    @abstractmethod
    async def register(self, request: RegisterRequest) -> RegisterResponse:
        pass

    @abstractmethod
    async def login(self, request: LoginRequest) -> LoginResponse:
        pass
