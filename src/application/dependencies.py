from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.application.contracts.user_service import IUserService
from src.application.services.user_service import UserService
from src.infrastructure.database import get_db_session

DBSessionDep = Annotated[AsyncSession, Depends(get_db_session)]


def get_user_service(db: DBSessionDep) -> IUserService:
    return UserService(db)
