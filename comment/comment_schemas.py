from typing import Union

from pydantic import BaseModel
from pydantic import BaseModel, Field, EmailStr
from reply.reply_schemas import Reply

class Comment(BaseModel):
    id: int = Field(None)
    content: str = Field(..., max_length=300)
    community_id: int = Field(...)
    creator_id: int = Field(...)
    replies: list[Reply] = []

    class Config:
        orm_mode = True