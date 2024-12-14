from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.future import select
from typing import TypeVar, Generic, Optional, List
from src.domain.entities.base_repository import IBaseRepository

T = TypeVar('T')


class BaseRepository(Generic[T], IBaseRepository[T]):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession], model: T):
        self.session_factory = session_factory
        self.model = model

    async def add(self, entity: T) -> T:
        async with self.session_factory() as db:
            db.add(entity)
            await db.commit()
            await db.refresh(entity)

            return entity

    async def get(self, entity_id: int) -> Optional[T]:
        async with self.session_factory() as db:
            entity = await db.get(self.model, entity_id)

            return entity

    async def get_all(self) -> List[T]:
        async with self.session_factory() as db:
            entities = await db.execute(select(self.model))
            entity_list = entities.scalars().all()

            return entity_list

    async def update(self, entity: T) -> T:
        async with self.session_factory() as db:
            await db.commit()
            await db.refresh(entity)

            return entity

    async def delete(self, entity_id: int) -> None:
        async with self.session_factory() as db:
            entity = await self.get(entity_id)
            if not entity:
                raise ValueError(f'Entity with id {entity_id} not found.')
            await db.delete(entity)
            await db.commit()
