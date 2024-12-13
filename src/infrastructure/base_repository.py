from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import TypeVar, Optional, List
from src.domain.entities.base_repository import IBaseRepository

T = TypeVar('T')


class BaseRepository(IBaseRepository[T]):
    def __init__(self, session: Session):
        self.db = session

    def add(self, entity: T) -> T:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)

        return entity

    def get_by_id(self, entity_id: int) -> Optional[T]:
        try:
            return self.db.query(T).filter_by(id=entity_id).one()
        except NoResultFound:
            return None

    def get_all(self) -> List[T]:
        return self.db.query(T).all()

    def update(self, entity: T) -> T:
        self.db.commit()
        self.db.refresh(entity)

        return entity

    def delete(self, entity_id: int) -> None:
        entity = self.get_by_id(entity_id)
        if not entity:
            raise ValueError(f'Entity with id {entity_id} not found.')
        self.db.delete(entity)
        self.db.commit()
