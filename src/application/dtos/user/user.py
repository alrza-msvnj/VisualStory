from pydantic import BaseModel, constr, EmailStr
from typing import Optional
from datetime import datetime


class UserRequest(BaseModel):
    username: constr(min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=8, max_length=128)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    profile_picture_url: Optional[str] = None
    bio: Optional[str] = None
    role: Optional[str] = "user"


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    password_hash: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    profile_picture_url: Optional[str] = None
    bio: Optional[str] = None
    join_date: datetime
    last_login: Optional[datetime] = None
    is_active: Optional[bool] = True
    role: Optional[str] = None

    class Config:
        from_attributes = True
