from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')


class IBaseRepository(ABC, Generic[T]):
    def __init__(self, session: Session, model: T):
        self.session = session
        self.model = model

    @abstractmethod
    def add(self, entity: T) -> T:
        pass

    @abstractmethod
    def get_by_id(self, entity_id: int) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> None:
        pass
