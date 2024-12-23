from typing import TypeVar, Generic, Optional, List
from abc import ABC, abstractmethod

T = TypeVar('T')


class IBaseRepository(Generic[T], ABC):

    @abstractmethod
    async def add(self, entity: T) -> T:
        pass

    @abstractmethod
    async def get(self, entity_id: int) -> Optional[T]:
        pass

    @abstractmethod
    async def get_all(self) -> List[T]:
        pass

    @abstractmethod
    async def update(self, entity: T) -> T:
        pass

    @abstractmethod
    async def delete(self, entity_id: int) -> None:
        pass
