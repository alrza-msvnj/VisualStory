from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import TypeVar, Generic, Optional, List
from src.domain.entities.base_repository import IBaseRepository

T = TypeVar('T')


class BaseRepository(Generic[T], IBaseRepository[T]):
    def __init__(self, db: AsyncSession, model: T):
        self.db = db
        self.model = model

    async def add(self, entity: T) -> T:
        self.db.add(entity)
        await self.db.commit()
        await self.db.refresh(entity)

        return entity

    async def get(self, entity_id: int) -> Optional[T]:
        entity = (await self.db.scalars(select(self.model).where(self.model.id == entity_id))).first()
        if not entity:
            raise HTTPException(status_code=404, detail="Entity not found")
        return entity

    async def get_all(self) -> List[T]:
        entities = await self.db.execute(select(self.model))
        entity_list = entities.scalars().all()

        return entity_list

    async def update(self, entity: T) -> T:
        await self.db.commit()
        await self.db.refresh(entity)

        return entity

    async def delete(self, entity_id: int) -> None:
        entity = await self.get(entity_id)
        if not entity:
            raise ValueError(f'Entity with id {entity_id} not found.')
        await self.db.delete(entity)
        await self.db.commit()
