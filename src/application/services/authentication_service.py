import os
import bcrypt
from dotenv import load_dotenv
from itsdangerous import URLSafeTimedSerializer
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.repositories.user_repository import UserRepository
from src.application.contracts.authentication_service import IAuthenticationService
from src.application.dtos.base_response_dto import BaseResponseDto
from src.application.dtos.authentication.register_dto import RegisterRequest, RegisterResponse
from src.application.dtos.authentication.login_dto import LoginRequest, LoginResponse
from src.domain.entities.user.user import User

load_dotenv()


class AuthenticationService(IAuthenticationService):
    def __init__(self, db: AsyncSession):
        self.user_repository = UserRepository(db)
        self.serializer = URLSafeTimedSerializer(os.getenv('SECRET_KEY'))

    async def register(self, request: RegisterRequest) -> RegisterResponse:
        # Check if user already exists
        existing_user = await self.user_repository.get_by_username(request.username)
        if existing_user:
            return BaseResponseDto(success=False, message='Username already exists')

        # Hash password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(request.password.encode('utf-8'), salt)

        # Create user entity
        user = User(
            username=request.username,
            email=request.email,
            password_hash=hashed_password.decode('utf-8'),
            first_name=request.first_name,
            last_name=request.last_name,
            role='user',
            profile_picture='default-avatar.png'
        )

        # Save user
        await self.user_repository.add(user)
        return RegisterResponse(success=True)

    async def login(self, request: LoginRequest) -> LoginResponse:
        # Get user by username
        user = await self.user_repository.get_by_username(request.username)
        if not user:
            return LoginResponse(success=False, message='Invalid credentials')

        # Verify password
        if not bcrypt.checkpw(request.password.encode('utf-8'),
                              user.password_hash.encode('utf-8')):
            return LoginResponse(success=False, message='Invalid credentials')

        # Create session
        session_data = self._create_session(user.id)

        return LoginResponse(success=True, value=session_data)

    def _create_session(self, user_id: int) -> str:
        return self.serializer.dumps({'user_id': user_id})

    def _validate_session(self, session_data):
        try:
            data = self.serializer.loads(session_data, max_age=3600)  # Expires in 1 hour
            return data
        except:
            return None
