from passlib.context import CryptContext
from datetime import datetime
from typing import List
from src.domain.entities.user.user import User
from src.infrastructure.database import session_factory
from src.application.dtos.user.user import UserRequest, UserResponse
from src.infrastructure.repositories.user_repository import UserRepository


class UserService:
    user_repository = UserRepository(session_factory)

    @classmethod
    async def add(cls, request: UserRequest) -> User:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        user = User(
            username=request.username,
            email=str(request.email),
            password_hash=pwd_context.hash(request.password),
            first_name=request.first_name,
            last_name=request.last_name,
            profile_picture_url=request.profile_picture_url,
            bio=request.bio,
            join_date=datetime.utcnow(),
            last_login=datetime.utcnow(),
            is_active=True,
            role='user'
        )
        user = await cls.user_repository.add(user)

        return user

    @classmethod
    async def get(cls, request: int) -> User:
        user = await cls.user_repository.get(request)

        new_user = UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            profile_picture_url=user.profile_picture_url,
            bio=user.bio,
            join_date=user.join_date,
            last_login=user.last_login,
            is_active=user.is_active,
            role=user.role
        )

        return new_user

    @classmethod
    async def get_all(cls) -> List[User]:
        users = await cls.user_repository.get_all()

        return users

    @classmethod
    async def get_by_username(cls, username: str) -> User:
        user = await cls.user_repository.get_by_username(username)

        return user
