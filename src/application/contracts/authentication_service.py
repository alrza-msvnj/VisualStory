from abc import ABC, abstractmethod
from src.application.dtos.authentication.register_dto import RegisterRequest, RegisterResponse
from src.application.dtos.authentication.login_dto import LoginRequest, LoginResponse


class IAuthenticationService(ABC):

    @abstractmethod
    async def register(self, request: RegisterRequest) -> RegisterResponse:
        pass

    @abstractmethod
    async def login(self, request: LoginRequest) -> LoginResponse:
        pass
