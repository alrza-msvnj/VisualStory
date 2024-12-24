from typing_extensions import TypeVar, Generic, List
from src.application.contracts.base_service import IBaseService

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')
W = TypeVar('W')


class BaseService(Generic[T, U, V, W], IBaseService[T, U]):
    def __init__(self, request_dto: T, response_dto: U, model: V, repository: W):
        self.request_dto = request_dto
        self.response_dto = response_dto
        self.model = model
        self.repository = repository

    async def add(self, entity: T) -> U:
        entity = self.model(**entity.dict())
        entity = await self.repository.add(entity)
        response = self.response_dto.model_validate(entity)
        return response

    async def get(self, entity_id: int) -> U:
        entity = await self.repository.get(entity_id)
        if entity is None:
            return None
        response = self.response_dto.model_validate(entity)
        return response

    async def get_all(self) -> List[U]:
        entities = await self.repository.get_all()
        response = [self.response_dto.model_validate(entity) for entity in entities]
        return response

    async def update(self, entity: T) -> U:
        entity = self.model(**entity.dict())
        entity = await self.repository.update(entity)
        response = self.response_dto.model_validate(entity)
        return response

    async def delete(self, entity_id: int) -> bool:
        response = await self.repository.delete(entity_id)
        return response
