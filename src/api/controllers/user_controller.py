from fastapi import APIRouter
from src.application.dtos.user.add_user import AddUserResponse, AddUserRequest
from src.application.services.user_service import UserService

router = APIRouter()


@router.post('/user', response_model=AddUserResponse)
def add(request: AddUserRequest):
    user = UserService.add(request)

    return user


@router.get('/user', response_model=AddUserRequest)
def get(request: int):
    user = UserService.get(request)

    return user
