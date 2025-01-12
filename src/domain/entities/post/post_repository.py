from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.entities.base_repository import IBaseRepository
from src.domain.entities.post.post import Post


class IPostRepository(IBaseRepository[Post], ABC):
    
    @abstractmethod
    async def get_by_user_id(self, user_id: int) -> List[Post]:
        pass
    
    @abstractmethod
    async def get_published_posts(self) -> List[Post]:
        pass
    
    @abstractmethod
    async def get_posts_by_tag(self, tag: str) -> List[Post]:
        pass
    
    @abstractmethod
    async def update_likes_count(self, post_id: int, increment: bool = True) -> Post:
        pass
