from pydantic import BaseModel
from src.application.dtos.base_response_dto import BaseResponseDto


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseResponseDto):
    value: str
