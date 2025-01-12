from fastapi import Depends, APIRouter
from src.application.contracts.authentication_service import IAuthenticationService
from src.application.dependencies import get_authentication_service
from src.application.dtos.authentication.register_dto import RegisterRequest, RegisterResponse
from src.application.dtos.authentication.login_dto import LoginRequest, LoginResponse
from src.application.dtos.authentication.logout_dto import LogoutRequest, LogoutResponse
from src.application.dtos.authentication.create_session_dto import CreateSessionRequest, CreateSessionResponse
from src.application.dtos.authentication.validate_session_dto import ValidateSessionRequest, ValidateSessionResponse


class AuthenticationController:
    def __init__(self):
        self.router = APIRouter(prefix="/api/auth", tags=["Authentication"])
        self.router.post("/register", response_model=RegisterResponse)(self.register)
        self.router.post("/login", response_model=LoginResponse)(self.login)
        self.router.post("/logout", response_model=LogoutResponse)(self.logout)
        self.router.post("/session", response_model=CreateSessionResponse)(self.create_session)
        self.router.post("/validate", response_model=ValidateSessionResponse)(self.validate_session)

    @staticmethod
    async def register(
        request: RegisterRequest,
        service: IAuthenticationService = Depends(get_authentication_service)
    ) -> RegisterResponse:
        return await service.register(request)

    @staticmethod
    async def login(
        request: LoginRequest,
        service: IAuthenticationService = Depends(get_authentication_service)
    ) -> LoginResponse:
        return await service.login(request)

    @staticmethod
    async def logout(
        request: LogoutRequest,
        service: IAuthenticationService = Depends(get_authentication_service)
    ) -> LogoutResponse:
        return await service.logout(request)

    @staticmethod
    async def create_session(
        request: CreateSessionRequest,
        service: IAuthenticationService = Depends(get_authentication_service)
    ) -> CreateSessionResponse:
        return await service.create_session(request)

    @staticmethod
    async def validate_session(
        request: ValidateSessionRequest,
        service: IAuthenticationService = Depends(get_authentication_service)
    ) -> ValidateSessionResponse:
        return await service.validate_session(request)