from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm.session import Session
from typing import Generic, Self, TypeVar, List, Optional

T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, db: Session):
        self.db = db

    def get(self, id: int) -> Optional[T]:
        return self.db.query(T).filter(T.id == id).first()

    def get_all(self) -> List[T]:
        return self.db.query(T).all()

    def add(self, entity: T) -> None:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        
    def update(self, entity: T) -> None:
        self.db.commit()
        self.db.refresh(entity)

    def delete(self, entity: T) -> None:
        self.db.delete(entity)
        self.db.commit()
