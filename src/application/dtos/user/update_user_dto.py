from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr


class UpdateUserRequest(BaseModel):
    id: int
    username: str
    email: EmailStr
    password_hash: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    bio: Optional[str] = None
    role: Optional[str] = "user"


class UpdateUserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    profile_picture_url: Optional[str] = None
    bio: Optional[str] = None
    join_date: datetime
    last_login: Optional[datetime] = None
    is_active: Optional[bool] = True
    role: Optional[str] = None
