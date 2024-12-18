from typing_extensions import TypeVar, Generic, List
from src.application.contracts.base_service import IBaseService

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')


class BaseService(Generic[T, U, V], IBaseService[T]):
    def __init__(self, response_dto: T, model: U, repository: V):
        self.response_dto = response_dto
        self.model = model
        self.repository = repository

    async def add(self, entity: T) -> T:
        entity = self.model(**self.response_dto.dict())
        entity = await self.repository.add(entity)
        response = self.response_dto.model_validate(entity)

        return response

    async def get(self, entity_id: int) -> T:
        entity = await self.repository.get(entity_id)
        response = self.response_dto.model_validate(entity)

        return response

    async def get_all(self) -> List[T]:
        entities = await self.repository.get_all()
        response = [self.response_dto.model_validate(entity) for entity in entities]

        return response

    async def update(self, entity: T) -> T:
        pass

    async def delete(self, entity_id: int) -> None:
        pass
