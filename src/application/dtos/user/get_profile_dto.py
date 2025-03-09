from typing import Optional
from pydantic import BaseModel


class GetProfileRequest(BaseModel):
    user_id: int


class GetProfileResponse(BaseModel):
    username: str
    profile_picture: Optional[str]
