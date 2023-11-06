import datetime
from pydantic import BaseModel, EmailStr, Field


class Link(BaseModel):
    url: str = Field(...)
    short_url: str = Field(...)


class LinkRes(Link):
    id: int = Field(default=None)
    created_at: datetime.datetime
    views: int


class LinkDB(BaseModel):
    id: int
    url: str
    short_url: str
    user: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    views: list
    is_active: int
    is_deleted: int
    is_blocked: int
    reports: int
