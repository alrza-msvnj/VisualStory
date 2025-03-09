from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class GetByUsernameRequest(BaseModel):
    username: str


class GetByUsernameResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    profile_picture: Optional[str] = None
    bio: Optional[str] = None
    join_date: datetime
    last_login: Optional[datetime] = None
    is_active: Optional[bool] = True
    role: Optional[str] = None
