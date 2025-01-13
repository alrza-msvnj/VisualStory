from pydantic import BaseModel, EmailStr
from src.application.dtos.base_response_dto import BaseResponseDto


class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    username: str
    password: str
    confirm_password: str


class RegisterResponse(BaseResponseDto):
    pass
