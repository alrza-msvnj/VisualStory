from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class AddPostRequest(BaseModel):
    caption: Optional[str]
    media_urls: List[str]
    media_type: str
    user_id: int
    location: Optional[str]
    tags: Optional[List[str]]
    visibility: str = 'public'

class AddPostResponse(BaseModel):
    id: int
    caption: Optional[str]
    media_urls: List[str]
    user_id: int
    created_at: datetime
