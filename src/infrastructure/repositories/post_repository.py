from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from src.domain.entities.post.post import Post
from src.domain.entities.post.post_repository import IPostRepository
from src.infrastructure.repositories.base_repository import BaseRepository


class PostRepository(BaseRepository[Post], IPostRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Post)

    async def get_posts_by_user_id(self, user_id: int) -> List[Post]:
        return (await self.db.scalars(
            select(Post)
            .where(Post.user_id == user_id)
            .order_by(Post.created_at.desc())
        )).all()
