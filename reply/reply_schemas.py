from typing import Union

from pydantic import BaseModel
from pydantic import BaseModel, Field, EmailStr

class Reply(BaseModel):
    id: int = Field(None)
    content: str = Field(..., max_length=300)
    comment_id: int = Field(...)
    
    class Config:
        orm_mode = True