from abc import ABC, abstractmethod
from typing import List
from src.application.dtos.post.add_post_dto import AddPostRequest, AddPostResponse
from src.application.dtos.post.get_post_dto import GetPostRequest, GetPostResponse
from src.application.dtos.post.get_all_post_dto import GetAllPostResponse
from src.application.dtos.post.update_post_dto import UpdatePostRequest, UpdatePostResponse
from src.application.dtos.post.delete_post_dto import DeletePostRequest, DeletePostResponse
from src.application.dtos.post.get_by_user_dto import GetByUserRequest, GetByUserResponse


class IPostService(ABC):
    @abstractmethod
    async def add(self, request: AddPostRequest) -> AddPostResponse:
        pass

    @abstractmethod
    async def get(self, request: GetPostRequest) -> GetPostResponse:
        pass

    @abstractmethod
    async def get_all(self) -> List[GetAllPostResponse]:
        pass

    @abstractmethod
    async def update(self, request: UpdatePostRequest) -> UpdatePostResponse:
        pass

    @abstractmethod
    async def delete(self, request: DeletePostRequest) -> DeletePostResponse:
        pass

    @abstractmethod
    async def get_by_user(self, request: GetByUserRequest) -> List[GetByUserResponse]:
        pass

    @abstractmethod
    async def update_likes_count(self, post_id: int, increment: bool = True) -> GetPostResponse:
        pass

    @abstractmethod
    async def update_comments_count(self, post_id: int, increment: bool = True) -> GetPostResponse:
        pass

    @abstractmethod
    async def get_posts_by_tag(self, tag: str) -> List[GetPostResponse]:
        pass

    @abstractmethod
    async def get_published_posts(self) -> List[GetPostResponse]:
        pass
