from sqlalchemy import (
    Integer,
    String,
    # mapped_column,
    DateTime,
    ForeignKey,
    Numeric,
    CheckConstraint,
)

from datetime import datetime

from sqlalchemy import String

# list
# from sqlalchemy import List
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    phone: Mapped[str] = mapped_column(String(50), nullable=True)
    address: Mapped[str] = mapped_column(String(50), nullable=True)
    town: Mapped[str] = mapped_column(String(50), nullable=True)
    created_on = mapped_column(DateTime(), default=datetime.now)
    updated_on = mapped_column(DateTime(), default=datetime.now, onupdate=datetime.now)
    photo = mapped_column(String(200), nullable=True)
    password = mapped_column(String(200), nullable=True)
    is_active: Mapped[int] = mapped_column(Integer, default=1)
    is_admin: Mapped[int] = mapped_column(Integer, default=0)
    is_staff: Mapped[int] = mapped_column(Integer, default=0)
    is_superuser: Mapped[int] = mapped_column(Integer, default=0)
    is_verified: Mapped[int] = mapped_column(Integer, default=0)
    is_deleted: Mapped[int] = mapped_column(Integer, default=0)
    is_blocked: Mapped[int] = mapped_column(Integer, default=0)
    is_suspended: Mapped[int] = mapped_column(Integer, default=0)
    is_premium: Mapped[int] = mapped_column(Integer, default=0)
    is_subscribed: Mapped[int] = mapped_column(Integer, default=0)
    is_trial: Mapped[int] = mapped_column(Integer, default=0)
    is_trial_used: Mapped[int] = mapped_column(Integer, default=0)
    is_trial_expired: Mapped[int] = mapped_column(Integer, default=0)

    def __repr__(self):
        return "<User(name='%s', last_name='%s', nickname='%s')>" % (
            self.first_name,
            self.last_name,
            self.username,
        )


class View(Base):
    __tablename__ = "view"
    user: Mapped[User] = mapped_column(Integer, ForeignKey("user.id"))
    link = mapped_column(Integer, ForeignKey("link.id"))
    created_at = mapped_column(DateTime(), default=datetime.now)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ip: Mapped[str] = mapped_column(String(50), nullable=True)
    device: Mapped[str] = mapped_column(String(50), nullable=True)
    os: Mapped[str] = mapped_column(String(50), nullable=True)
    browser: Mapped[str] = mapped_column(String(50), nullable=True)
    country: Mapped[str] = mapped_column(String(50), nullable=True)
    city: Mapped[str] = mapped_column(String(50), nullable=True)


class Link(Base):
    __tablename__ = "link"
    url: Mapped[str] = mapped_column(String(400))
    short_url: Mapped[str] = mapped_column(String(50), primary_key=True)
    user: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    created_at = mapped_column(DateTime(), default=datetime.now)
    updated_at = mapped_column(DateTime(), default=datetime.now, onupdate=datetime.now)
    views = None
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    is_active: Mapped[int] = mapped_column(Integer, default=1)
    is_deleted: Mapped[int] = mapped_column(Integer, default=0)
    is_blocked: Mapped[int] = mapped_column(Integer, default=0)
    reports: Mapped[int] = mapped_column(Integer, default=0)


def create_tables(engine):
    # create tables for User, Link and View
    Base.metadata.create_all(engine)
