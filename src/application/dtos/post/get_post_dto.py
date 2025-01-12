from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class GetPostRequest(BaseModel):
    id: int

class GetPostResponse(BaseModel):
    id: int
    caption: Optional[str]
    media_urls: List[str]
    media_type: str
    created_at: datetime
    updated_at: datetime
    user_id: int
    likes_count: int
    comments_count: int
    location: Optional[str]
    tags: Optional[List[str]]
    visibility: str
