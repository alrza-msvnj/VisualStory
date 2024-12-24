from pydantic import BaseModel, ConfigDict


class DeleteUserRequest(BaseModel):
    id: int


class DeleteUserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    deleted: bool
