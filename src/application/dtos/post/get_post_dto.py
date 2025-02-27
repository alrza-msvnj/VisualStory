from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

class GetPostRequest(BaseModel):
    id: int

class GetPostResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    content: str
    image_url: Optional[str]
    created_at: datetime
    updated_at: datetime
    user_id: int
    is_deleted: bool
