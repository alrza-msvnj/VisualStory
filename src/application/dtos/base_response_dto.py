from typing import Optional
from pydantic import BaseModel


class BaseResponseDto(BaseModel):
    success: bool
    message: Optional[str]
