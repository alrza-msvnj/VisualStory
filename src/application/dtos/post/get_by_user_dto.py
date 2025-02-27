from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class GetByUserRequest(BaseModel):
    user_id: int

class GetByUserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    content: str
    image_url: Optional[str]
    created_at: datetime
    updated_at: datetime
    user_id: int
    is_deleted: bool
