from passlib.context import CryptContext
from datetime import datetime, timezone
from src.domain.entities.user.user import User
from src.infrastructure.database import session
from src.application.dtos.user.add_user import AddUserRequest, AddUserResponse
from src.infrastructure.repositories.user_repository import UserRepository


class UserService:
    user_repository = UserRepository(session)

    @classmethod
    def add(cls, request: AddUserRequest) -> User:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        user = User(
            username=request.username,
            email=str(request.email),
            password_hash=pwd_context.hash(request.password),
            first_name=request.first_name,
            last_name=request.last_name,
            profile_picture_url=request.profile_picture_url,
            bio=request.bio,
            join_date=datetime.now(timezone.utc),
            last_login=datetime.now(timezone.utc),
            is_active=True,
            role='user'
        )
        user = cls.user_repository.add(user)

        return user

    @classmethod
    def get(cls, request: int) -> User:
        user = cls.user_repository.get_by_id(request)

        return user
