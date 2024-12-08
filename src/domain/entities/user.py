from dataclasses import dataclass
from typing import Optional
from base_entity import BaseEntity

@dataclass
class User(BaseEntity):
    username: str
    email: str
    bio: Optional[str] = None
    profile_image_url: Optional[str] = None