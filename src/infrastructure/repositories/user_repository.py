from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import Optional
from src.infrastructure.base_repository import BaseRepository
from src.domain.entities.user.user import User


class UserRepository(BaseRepository[User]):
    def __init__(self, session: Session):
        super().__init__(session)

    def get_by_username(self, username: str) -> Optional[User]:
        try:
            return self.db.query(User).filter_by(username=username).one()
        except NoResultFound:
            return None

    def get_by_email(self, email: str) -> Optional[User]:
        try:
            return self.db.query(User).filter_by(email=email).one()
        except NoResultFound:
            return None
