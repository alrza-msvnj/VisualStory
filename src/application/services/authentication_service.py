from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.repositories.user_repository import UserRepository
from src.application.contracts.authentication_service import IAuthenticationService
from src.application.dtos.authentication.register_dto import RegisterRequest, RegisterResponse
from src.application.dtos.authentication.login_dto import LoginRequest, LoginResponse
from src.application.dtos.authentication.logout_dto import LogoutRequest, LogoutResponse
from src.application.dtos.authentication.create_session_dto import CreateSessionRequest, CreateSessionResponse
from src.application.dtos.authentication.validate_session_dto import ValidateSessionRequest, ValidateSessionResponse
from src.domain.entities.user.user import User
import bcrypt
import jwt
from datetime import datetime, timedelta

class AuthenticationService(IAuthenticationService):
    def __init__(self, db: AsyncSession):
        self.user_repository = UserRepository(db)
        self.secret_key = "your-secret-key"  # Move to configuration
        self.session_duration = timedelta(hours=24)

    async def register(self, request: RegisterRequest) -> RegisterResponse:
        # Check if user already exists
        existing_user = await self.user_repository.get_by_username(request.username)
        if existing_user:
            return RegisterResponse(success=False, message="Username already exists")

        # Hash password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(request.password.encode('utf-8'), salt)

        # Create user entity
        user = User(
            username=request.username,
            email=request.email,
            password_hash=hashed_password.decode('utf-8'),
            full_name=request.full_name,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        # Save user
        created_user = await self.user_repository.add(user)
        
        return RegisterResponse(
            success=True,
            user_id=created_user.id,
            username=created_user.username
        )

    async def login(self, request: LoginRequest) -> LoginResponse:
        # Get user by username
        user = await self.user_repository.get_by_username(request.username)
        if not user:
            return LoginResponse(success=False, message="Invalid credentials")

        # Verify password
        if not bcrypt.checkpw(request.password.encode('utf-8'), 
                            user.password_hash.encode('utf-8')):
            return LoginResponse(success=False, message="Invalid credentials")

        # Generate token
        token = self._generate_token(user.id)

        return LoginResponse(
            success=True,
            token=token,
            user_id=user.id,
            username=user.username
        )

    async def logout(self, request: LogoutRequest) -> LogoutResponse:
        # Here you could implement token blacklisting if needed
        return LogoutResponse(success=True)

    async def create_session(self, request: CreateSessionRequest) -> CreateSessionResponse:
        try:
            # Validate token
            payload = jwt.decode(request.token, self.secret_key, algorithms=["HS256"])
            user_id = payload.get('user_id')
            
            # Get user
            user = await self.user_repository.get(user_id)
            if not user:
                return CreateSessionResponse(success=False, message="Invalid token")

            return CreateSessionResponse(
                success=True,
                user_id=user.id,
                username=user.username,
                session_id=request.token
            )

        except jwt.ExpiredSignatureError:
            return CreateSessionResponse(success=False, message="Token expired")
        except jwt.InvalidTokenError:
            return CreateSessionResponse(success=False, message="Invalid token")

    async def validate_session(self, request: ValidateSessionRequest) -> ValidateSessionResponse:
        try:
            # Validate token
            payload = jwt.decode(request.session_id, self.secret_key, algorithms=["HS256"])
            user_id = payload.get('user_id')
            
            # Get user
            user = await self.user_repository.get(user_id)
            if not user:
                return ValidateSessionResponse(success=False, message="Invalid session")

            return ValidateSessionResponse(
                success=True,
                user_id=user.id,
                username=user.username
            )

        except jwt.ExpiredSignatureError:
            return ValidateSessionResponse(success=False, message="Session expired")
        except jwt.InvalidTokenError:
            return ValidateSessionResponse(success=False, message="Invalid session")

    def _generate_token(self, user_id: int) -> str:
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + self.session_duration,
            'iat': datetime.utcnow()
        }
        return jwt.encode(payload, self.secret_key, algorithm="HS256")

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
