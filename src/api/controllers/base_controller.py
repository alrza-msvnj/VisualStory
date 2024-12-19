from fastapi import APIRouter, status
from typing import Generic, TypeVar, List

TEntity = TypeVar("TEntity")
TService = TypeVar("TService", bound="BaseService")


class BaseController(Generic[TEntity, TService]):
    def __init__(self, service: TService):
        self.service = service
        self.router = APIRouter()

        self.router.post("/", response_model=TEntity)(self.add)
        self.router.get("/{id}", response_model=TEntity)(self.get)
        self.router.get("/", response_model=List[TEntity])(self.get_all)
        self.router.put("/{id}", response_model=TEntity)(self.update)
        self.router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)(self.delete)

    async def add(self, entity: TEntity) -> TEntity:
        entity = await self.service.add(entity)

        return entity

    async def get(self, entity_id: int) -> TEntity:
        entity = await self.service.get(entity_id)

        return entity

    async def get_all(self) -> List[TEntity]:
        entities = await self.service.get_all()

        return entities

    async def update(self, entity: TEntity) -> TEntity:
        entity = await self.service.update(entity)

        return entity

    async def delete(self, entity_id: int) -> None:
        await self.service.delete(entity_id)
