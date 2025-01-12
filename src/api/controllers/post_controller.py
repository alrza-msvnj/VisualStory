from typing import List
from fastapi import Depends, APIRouter
from src.application.contracts.post_service import IPostService
from src.application.dependencies import get_post_service
from src.application.dtos.post.add_post_dto import AddPostRequest, AddPostResponse
from src.application.dtos.post.get_post_dto import GetPostRequest, GetPostResponse
from src.application.dtos.post.get_all_post_dto import GetAllPostResponse
from src.application.dtos.post.update_post_dto import UpdatePostRequest, UpdatePostResponse
from src.application.dtos.post.delete_post_dto import DeletePostRequest, DeletePostResponse
from src.application.dtos.post.get_by_user_dto import GetByUserRequest, GetByUserResponse


class PostController:
    def __init__(self):
        self.router = APIRouter(prefix="/api/post", tags=["Post"])
        self.router.post("/", response_model=AddPostResponse)(self.add)
        self.router.get("/{id}", response_model=GetPostResponse)(self.get)
        self.router.get("/", response_model=List[GetAllPostResponse])(self.get_all)
        self.router.put("/", response_model=UpdatePostResponse)(self.update)
        self.router.delete("/{id}", response_model=DeletePostResponse)(self.delete)
        self.router.get("/user/{user_id}", response_model=List[GetByUserResponse])(self.get_by_user)
        self.router.post("/{post_id}/like")(self.like_post)
        self.router.post("/{post_id}/unlike")(self.unlike_post)
        self.router.get("/tag/{tag}", response_model=List[GetPostResponse])(self.get_posts_by_tag)
        self.router.get("/published", response_model=List[GetPostResponse])(self.get_published_posts)

    @staticmethod
    async def add(
        post: AddPostRequest, 
        service: IPostService = Depends(get_post_service)
    ) -> AddPostResponse:
        return await service.add(post)

    @staticmethod
    async def get(
        post_id: int, 
        service: IPostService = Depends(get_post_service)
    ) -> GetPostResponse:
        return await service.get(GetPostRequest(id=post_id))

    @staticmethod
    async def get_all(
        service: IPostService = Depends(get_post_service)
    ) -> List[GetAllPostResponse]:
        return await service.get_all()

    @staticmethod
    async def update(
        post: UpdatePostRequest, 
        service: IPostService = Depends(get_post_service)
    ) -> UpdatePostResponse:
        return await service.update(post)

    @staticmethod
    async def delete(
        post_id: int, 
        service: IPostService = Depends(get_post_service)
    ) -> DeletePostResponse:
        return await service.delete(DeletePostRequest(id=post_id))

    @staticmethod
    async def get_by_user(
        user_id: int, 
        service: IPostService = Depends(get_post_service)
    ) -> List[GetByUserResponse]:
        return await service.get_by_user(GetByUserRequest(user_id=user_id))

    @staticmethod
    async def like_post(
        post_id: int, 
        service: IPostService = Depends(get_post_service)
    ) -> GetPostResponse:
        return await service.update_likes_count(post_id, increment=True)

    @staticmethod
    async def unlike_post(
        post_id: int, 
        service: IPostService = Depends(get_post_service)
    ) -> GetPostResponse:
        return await service.update_likes_count(post_id, increment=False)

    @staticmethod
    async def get_posts_by_tag(
        tag: str, 
        service: IPostService = Depends(get_post_service)
    ) -> List[GetPostResponse]:
        return await service.get_posts_by_tag(tag)

    @staticmethod
    async def get_published_posts(
        service: IPostService = Depends(get_post_service)
    ) -> List[GetPostResponse]:
        return await service.get_published_posts()
