from pydantic import BaseModel


class SaveProfilePictureRequest(BaseModel):
    user_id: int
    profile_picture: str


class SaveProfilePictureResponse(BaseModel):
    success: bool
