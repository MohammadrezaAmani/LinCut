from pydantic import BaseModel, EmailStr, Field


class Link(BaseModel):
    url: str = Field(...)
    short_url: str = Field(...)


class LinkRes(Link):
    id: int = Field(default=None)
    created_at: str = Field(...)
    views: int


class LinkDB(LinkRes):
    updated_at: str = Field(...)
    user_id: int
