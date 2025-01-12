from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.entities.post.post import Post
from src.infrastructure.repositories.post_repository import PostRepository
from src.application.contracts.post_service import IPostService
from src.application.dtos.post.add_post_dto import AddPostRequest, AddPostResponse
from src.application.dtos.post.get_post_dto import GetPostRequest, GetPostResponse
from src.application.dtos.post.get_all_post_dto import GetAllPostResponse
from src.application.dtos.post.update_post_dto import UpdatePostRequest, UpdatePostResponse
from src.application.dtos.post.delete_post_dto import DeletePostRequest, DeletePostResponse
from src.application.dtos.post.get_by_user_dto import GetByUserRequest, GetByUserResponse


class PostService(IPostService):
    def __init__(self, db: AsyncSession):
        self.post_repository = PostRepository(db)

    async def add(self, request: AddPostRequest) -> AddPostResponse:
        post = Post(**request.model_dump())
        post = await self.post_repository.add(post)
        response = AddPostResponse.model_validate(post)
        return response

    async def get(self, request: GetPostRequest) -> GetPostResponse:
        post = await self.post_repository.get(request.id)
        response = GetPostResponse.model_validate(post)
        return response

    async def get_all(self) -> List[GetAllPostResponse]:
        posts = await self.post_repository.get_all()
        response = [GetAllPostResponse.model_validate(post) for post in posts]
        return response

    async def update(self, request: UpdatePostRequest) -> UpdatePostResponse:
        post = Post(**request.model_dump())
        post = await self.post_repository.update(post)
        response = UpdatePostResponse.model_validate(post)
        return response

    async def delete(self, request: DeletePostRequest) -> DeletePostResponse:
        response = await self.post_repository.delete(request.id)
        return DeletePostResponse(deleted=response)

    async def get_by_user(self, request: GetByUserRequest) -> List[GetByUserResponse]:
        posts = await self.post_repository.get_by_user_id(request.user_id)
        response = [GetByUserResponse.model_validate(post) for post in posts]
        return response

    async def update_likes_count(self, post_id: int, increment: bool = True) -> GetPostResponse:
        post = await self.post_repository.update_likes_count(post_id, increment)
        response = GetPostResponse.model_validate(post)
        return response

    async def update_comments_count(self, post_id: int, increment: bool = True) -> GetPostResponse:
        post = await self.post_repository.update_comments_count(post_id, increment)
        response = GetPostResponse.model_validate(post)
        return response

    async def get_posts_by_tag(self, tag: str) -> List[GetPostResponse]:
        posts = await self.post_repository.get_posts_by_tag(tag)
        response = [GetPostResponse.model_validate(post) for post in posts]
        return response

    async def get_published_posts(self) -> List[GetPostResponse]:
        posts = await self.post_repository.get_published_posts()
        response = [GetPostResponse.model_validate(post) for post in posts]
        return response