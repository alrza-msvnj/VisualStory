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

    async def get_by_user_id(self, user_id: int) -> List[Post]:
        return (await self.db.scalars(
            select(Post)
            .where(Post.user_id == user_id)
            .order_by(Post.created_at.desc())
        )).all()

    async def get_published_posts(self) -> List[Post]:
        return (await self.db.scalars(
            select(Post)
            .where(Post.is_published == True)
            .order_by(Post.created_at.desc())
        )).all()

    async def get_posts_by_tag(self, tag: str) -> List[Post]:
        return (await self.db.scalars(
            select(Post)
            .where(Post.tags.contains([tag]))
            .where(Post.is_published == True)
            .order_by(Post.created_at.desc())
        )).all()

    async def update_likes_count(self, post_id: int, increment: bool = True) -> Optional[Post]:
        post = await self.get(post_id)
        if not post:
            return None
            
        delta = 1 if increment else -1
        await self.db.execute(
            update(Post)
            .where(Post.id == post_id)
            .values(likes_count=Post.likes_count + delta)
        )
        await self.db.commit()
        return await self.get(post_id)

    async def update_comments_count(self, post_id: int, increment: bool = True) -> Optional[Post]:
        post = await self.get(post_id)
        if not post:
            return None
            
        delta = 1 if increment else -1
        await self.db.execute(
            update(Post)
            .where(Post.id == post_id)
            .values(comments_count=Post.comments_count + delta)
        )
        await self.db.commit()
        return await self.get(post_id)

