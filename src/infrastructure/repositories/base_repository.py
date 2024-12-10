from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import Optional, List
from src.domain.entities.base_repository import IBaseRepository


class BaseRepository(IBaseRepository):
    def __init__(self, session: Session, model: type):
        super().__init__(session, model)

    def add(self, entity) -> object:
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)

        return entity

    def get_by_id(self, entity_id: int) -> Optional[object]:
        try:
            return self.session.query(self.model).filter_by(id=entity_id).one()
        except NoResultFound:
            return None

    def get_all(self) -> List[object]:
        return self.session.query(self.model).all()

    def update(self, entity) -> object:
        self.session.commit()
        self.session.refresh(entity)

        return entity

    def delete(self, entity_id) -> None:
        entity = self.get_by_id(entity_id)
        if entity:
            self.session.delete(entity)
            self.session.commit()
