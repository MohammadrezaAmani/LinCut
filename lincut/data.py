from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from .database.mainDB import User, create_tables


class UserCache:
    def __init__(self):
        self.users = {}  # int id -> UserRecord

    def add_user(self, user):
        self.users[user.id] = user

    @property
    def total_users(self):
        return len(self.users)

    def remove_user(self, user_id: int):
        if user_id not in self.users:
            return None

        user = self.users[user_id]
        del self.users[user_id]
        return user


def start():
    engine = create_engine("sqlite:///ecommadb.db")
    create_tables(engine)
    session = scoped_session(
        sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
    )

    # adding users
    usercache = UserCache()
    for user in session.query(User).all():
        usercache.add_user(user)

    return (session, usercache)


SESSION, usercache = start()
