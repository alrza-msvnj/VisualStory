from pydantic import BaseModel
from src.application.dtos.base_response_dto import BaseResponseDto


class RegisterRequest(BaseModel):
    pass


class RegisterResponse(BaseResponseDto):
    pass
