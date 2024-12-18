from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar('T')


class IBaseService(Generic[T], ABC):
    @abstractmethod
    async def add(self, entity: T) -> T:
        pass

    @abstractmethod
    async def get(self, entity_id: int) -> T:
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
