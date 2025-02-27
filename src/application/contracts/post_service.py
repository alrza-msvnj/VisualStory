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
    async def get_posts_by_user_id(self, request: GetByUserRequest) -> List[GetByUserResponse]:
        pass
