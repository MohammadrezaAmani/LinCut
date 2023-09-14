from pydantic import BaseModel
import datetime


class View(BaseModel):
    link: int
    created_at: datetime.datetime
    id: int
    ip: str = None
    device: str = None
    os: str = None
    browser: str = None
    country: str = None
    city: str = None


class ViewDB(View):
    user: int
