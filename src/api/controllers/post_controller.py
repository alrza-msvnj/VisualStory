import os
from typing import List
from dotenv import load_dotenv
from fastapi import Depends, APIRouter, Request, HTTPException
from itsdangerous import URLSafeTimedSerializer
from src.application.contracts.post_service import IPostService
from src.application.dependencies import get_post_service
from src.application.dtos.post.add_post_dto import AddPostRequest, AddPostResponse
from src.application.dtos.post.get_post_dto import GetPostRequest, GetPostResponse
from src.application.dtos.post.get_all_post_dto import GetAllPostResponse
from src.application.dtos.post.update_post_dto import UpdatePostRequest, UpdatePostResponse
from src.application.dtos.post.delete_post_dto import DeletePostRequest, DeletePostResponse
from src.application.dtos.post.get_by_user_dto import GetByUserRequest, GetByUserResponse

load_dotenv()


class PostController:
    def __init__(self):
        self.router = APIRouter(prefix="/api/post", tags=["Post"])
        self.router.post("/", response_model=AddPostResponse)(self.add)
        self.router.get("/{id}", response_model=GetPostResponse)(self.get)
        self.router.get("/", response_model=List[GetAllPostResponse])(self.get_all)
        self.router.put("/", response_model=UpdatePostResponse)(self.update)
        self.router.delete("/{id}", response_model=DeletePostResponse)(self.delete)
        self.router.get("/get_posts_by_user_id/{user_id}", response_model=List[GetByUserResponse])(self.get_posts_by_user_id)

    @staticmethod
    async def add(request: Request, service: IPostService = Depends(get_post_service)) -> AddPostResponse:
        serializer = URLSafeTimedSerializer(os.getenv('SECRET_KEY'))
        session_id = request.cookies.get('session_id')
        if not session_id:
            raise HTTPException(status_code=400, detail="Login required")
        session = serializer.loads(session_id)

        body = await request.json()
        post = AddPostRequest(
            content=body['content'],
            user_id=session['user_id']
        )

        return await service.add(post)

    @staticmethod
    async def get(post_id: int, service: IPostService = Depends(get_post_service)) -> GetPostResponse:
        return await service.get(GetPostRequest(id=post_id))

    @staticmethod
    async def get_all(service: IPostService = Depends(get_post_service)) -> List[GetAllPostResponse]:
        return await service.get_all()

    @staticmethod
    async def update(request: UpdatePostRequest, service: IPostService = Depends(get_post_service)) -> UpdatePostResponse:
        return await service.update(request)

    @staticmethod
    async def delete(post_id: int, service: IPostService = Depends(get_post_service)) -> DeletePostResponse:
        return await service.delete(DeletePostRequest(id=post_id))

    @staticmethod
    async def get_posts_by_user_id(user_id: int, service: IPostService = Depends(get_post_service)) -> List[GetByUserResponse]:
        return await service.get_posts_by_user(GetByUserRequest(user_id=user_id))
