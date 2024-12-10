from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from src.domain.entities.base_repository import IBaseRepository
from src.domain.entities.user.user import User


class IUserRepository(IBaseRepository[User], ABC):
    def __init__(self, session: Session):
        super().__init__(session, User)

    @abstractmethod
    def get_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass
