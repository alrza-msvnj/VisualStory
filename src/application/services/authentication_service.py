from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.repositories.user_repository import UserRepository
from src.application.contracts.authentication_service import IAuthenticationService
from src.application.dtos.authentication.register_dto import RegisterRequest, RegisterResponse
from src.application.dtos.authentication.login_dto import LoginRequest, LoginResponse
from src.application.dtos.authentication.logout_dto import LogoutRequest, LogoutResponse
from src.application.dtos.authentication.create_session_dto import CreateSessionRequest, CreateSessionResponse
from src.application.dtos.authentication.validate_session_dto import ValidateSessionRequest, ValidateSessionResponse


class AuthenticationService(IAuthenticationService):
    def __init__(self, db: AsyncSession):
        self.user_repository = UserRepository(db)

    async def register(self, request: RegisterRequest) -> RegisterResponse:
        pass

    async def login(self, request: LoginRequest) -> LoginResponse:
        pass

    async def logout(self, request: LogoutRequest) -> LogoutResponse:
        pass

    async def create_session(self, request: CreateSessionRequest) -> CreateSessionResponse:
        pass

    async def validate_session(self, request: ValidateSessionRequest) -> ValidateSessionResponse:
        pass
