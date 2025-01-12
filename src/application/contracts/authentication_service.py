from abc import ABC, abstractmethod
from src.application.dtos.authentication.register_dto import RegisterRequest, RegisterResponse
from src.application.dtos.authentication.login_dto import LoginRequest, LoginResponse
from src.application.dtos.authentication.logout_dto import LogoutRequest, LogoutResponse
from src.application.dtos.authentication.create_session_dto import CreateSessionRequest, CreateSessionResponse
from src.application.dtos.authentication.validate_session_dto import ValidateSessionRequest, ValidateSessionResponse


class IAuthenticationService(ABC):

    @abstractmethod
    async def register(self, request: RegisterRequest) -> RegisterResponse:
        pass

    @abstractmethod
    async def login(self, request: LoginRequest) -> LoginResponse:
        pass

    @abstractmethod
    async def logout(self, request: LogoutRequest) -> LogoutResponse:
        pass

    @abstractmethod
    async def create_session(self, request: CreateSessionRequest) -> CreateSessionResponse:
        pass

    @abstractmethod
    async def validate_session(self, request: ValidateSessionRequest) -> ValidateSessionResponse:
        pass
