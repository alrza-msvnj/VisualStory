from pydantic import BaseModel

class DeletePostRequest(BaseModel):
    id: int

class DeletePostResponse(BaseModel):
    deleted: bool
