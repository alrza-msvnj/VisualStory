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
        if entity.id == 0:
            entity.id = None
        self.db.add(entity)
        await self.db.commit()
        await self.db.refresh(entity)
        return entity

    async def get(self, entity_id: int) -> Optional[T]:
        return (await self.db.execute(select(self.model).filter(self.model.id == entity_id))).scalars().first()

    async def get_all(self) -> List[T]:
        return (await self.db.execute(select(self.model))).scalars().all()

    async def update(self, entity: T) -> T:
        existed_entity = await self.get(entity.id)
        if not existed_entity:
            return None
        for key in vars(entity).keys():
            if not key.startswith("_") and hasattr(existed_entity, key):
                value = getattr(entity, key)
                setattr(existed_entity, key, value)
        await self.db.commit()
        await self.db.refresh(existed_entity)
        return existed_entity

    async def delete(self, entity_id: int) -> bool:
        entity = await self.get(entity_id)
        if entity:
            await self.db.delete(entity)
            await self.db.commit()
            return True
        return False
