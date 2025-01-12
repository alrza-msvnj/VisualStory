from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class GetByUserRequest(BaseModel):
    user_id: int

class GetByUserResponse(BaseModel):
    id: int
    caption: Optional[str]
    media_urls: List[str]
    media_type: str
    created_at: datetime
    likes_count: int
    comments_count: int
