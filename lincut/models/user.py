from pydantic import BaseModel, EmailStr, Field


class UserLogin(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)


class UserSignUp(UserLogin):
    confirmPassword: str = Field(...)
    phone: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)


class UserSchema(BaseModel):
    id: int = Field(default=None)
    email: EmailStr = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    phone_number: str
    address: str = None
    city: str = None
    state: str = None
    country: str = None
    gender: str = None
    date_of_birth: str = None


class UserInDBSchema(BaseModel):
    id: int = Field(default=None)
    email: EmailStr = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    password: str = Field(...)
    phone_number: str
    address: str = None
    city: str = None
    state: str = None
    country: str = None
    gender: str = None
    date_of_birth: str = None
