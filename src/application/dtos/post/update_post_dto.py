from pydantic import BaseModel
from typing import Optional, List

class UpdatePostRequest(BaseModel):
    id: int
    caption: Optional[str]
    media_urls: Optional[List[str]]
    location: Optional[str]
    tags: Optional[List[str]]
    visibility: Optional[str]

class UpdatePostResponse(BaseModel):
    id: int
    caption: Optional[str]
    media_urls: List[str]
    visibility: str
