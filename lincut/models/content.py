from pydantic import BaseModel, EmailStr, Field


class Link(BaseModel):
    url: str = Field(...)
    short_url: str = Field(...)


class LinkDB(Link):
    id: int = Field(default=None)
    created_at: str = Field(...)
    updated_at: str = Field(...)
    user_id: int
    deleted_at: str
