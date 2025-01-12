from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.application.contracts.user_service import IUserService
from src.application.services.user_service import UserService
from src.application.contracts.authentication_service import IAuthenticationService
from src.application.services.authentication_service import AuthenticationService
from src.application.contracts.post_service import IPostService
from src.application.services.post_service import PostService
from src.infrastructure.database import get_db_session

DBSessionDep = Annotated[AsyncSession, Depends(get_db_session)]


def get_user_service(db: DBSessionDep) -> IUserService:
    return UserService(db)


def get_authentication_service(db: DBSessionDep) -> IAuthenticationService:
    return AuthenticationService(db)


def get_post_service(db: DBSessionDep) -> IPostService:
    return PostService(db)