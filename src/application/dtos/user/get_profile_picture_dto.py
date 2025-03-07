from typing import Optional

from pydantic import BaseModel


class GetProfilePictureRequest(BaseModel):
    user_id: int


class GetProfilePictureResponse(BaseModel):
    profile_picture: Optional[str]
