from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.entities.base_repository import IBaseRepository
from src.domain.entities.post.post import Post


class IPostRepository(IBaseRepository[Post], ABC):
    
    @abstractmethod
    async def get_posts_by_user_id(self, user_id: int) -> List[Post]:
        pass
