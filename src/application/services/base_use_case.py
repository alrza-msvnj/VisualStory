from typing import Generic, TypeVar
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

T = TypeVar('T')

class BaseUseCase(Generic[T], ABC):
    def __init__(self, db: Session):
        self.db = db


