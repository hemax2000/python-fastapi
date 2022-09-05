from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Response(BaseModel):
    id: str
    title: str
    created_at: datetime
    completed: bool
    page_num: int

    class Config:
        orm_mode = True


class CreateRequest(BaseModel):
    title: str


class UpdateRequest(BaseModel):
    title: str
