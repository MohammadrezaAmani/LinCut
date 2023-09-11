from pydantic import BaseModel, EmailStr, Field


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"


class RefreshToken(BaseModel):
    access_token: str


class Token(RefreshToken):
    refresh_token: str
