from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar('T')
U = TypeVar('U')


class IBaseService(Generic[T, U], ABC):

    @abstractmethod
    async def add(self, entity: T) -> U:
        pass

    @abstractmethod
    async def get(self, entity_id: int) -> U:
        pass

    @abstractmethod
    async def get_all(self) -> List[U]:
        pass

    @abstractmethod
    async def update(self, entity: T) -> U:
        pass

    @abstractmethod
    async def delete(self, entity_id: int) -> bool:
        pass
