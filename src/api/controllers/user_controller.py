from fastapi import APIRouter
from typing import List
from src.application.dtos.user.user import UserResponse, UserRequest
from src.application.services.user_service import UserService

router = APIRouter()


@router.post('/user/add', response_model=UserResponse)
async def add(request: UserRequest):
    user = await UserService.add(request)

    return user


@router.get('/user/get', response_model=UserResponse)
async def get(request: int):
    user = await UserService.get(request)

    return user


@router.get('/user/get_all', response_model=List[UserResponse])
async def get_all():
    user = await UserService.get_all()

    return user


@router.get('/user/get_by_username', response_model=UserResponse)
async def get_by_username(username: str):
    user = await UserService.get_by_username(username)

    return user
