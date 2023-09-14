from pydantic import BaseModel, EmailStr
import datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserSignUp(UserLogin):
    first_name: str
    last_name: str
    username: str
    phone: str
    address: str
    town: str
    photo: str


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    phone: EmailStr
    address: str
    town: str
    created_on: datetime.datetime
    updated_on: datetime.datetime
    photo: str
    is_active: int
    is_admin: int
    is_staff: int
    is_superuser: int
    is_verified: int
    is_deleted: int
    is_blocked: int
    is_suspended: int
    is_premium: int
    is_subscribed: int
    is_trial: int
    is_trial_used: int
    is_trial_expired: int


class UserDB(User):
    password: str
