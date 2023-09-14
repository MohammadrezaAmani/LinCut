import threading
from ecomma.data import SESSION, usercache
from datetime import datetime, timedelta
from .mainDB import User
from ecomma.models.user import UserDB

USER_INSERTION_LOCK = threading.RLock()


def add_user(id: int):
    with USER_INSERTION_LOCK:
        user = SESSION.query(User).filter(User.id == id).first()
        if user:
            SESSION.expunge(user)
            SESSION.close()
            return user
        user = User(id)
        usercache.add_user(user)
        print(f"added user: {str(user)}")
        SESSION.add(user)
        SESSION.commit()
        SESSION.close()
        return user


def add_user_object(user: User):
    with USER_INSERTION_LOCK:
        prev_user = SESSION.query(User).filter(User.id == user.id).first()
        if prev_user:
            SESSION.close()
            return False
        user = UserToUser(user)
        SESSION.add(user)
        SESSION.commit()
        SESSION.close()
        return True


def get_user(id: int):
    return SESSION.query(User).filter(User.id == id).first()


def count_active_users(minutes: int):
    return (
        SESSION.query(User)
        .filter(User.last_active >= datetime.utcnow() - timedelta(minutes=minutes))
        .count()
    )


def count_new_signups(minutes: int):
    return (
        SESSION.query(User)
        .filter(User.signup_date >= datetime.utcnow() - timedelta(minutes=minutes))
        .count()
    )


def list_users():
    return SESSION.query(User).all()


def count_users():
    return len(usercache.users)


def authenicate(email: str, password: str):
    return (
        SESSION.query(User)
        .filter(User.email == email, User.password == password)
        .first()
    )


def searchUserByEmail(email: str):
    return SESSION.query(User).filter(User.email == email).first()


def searchUserById(id: int):
    return SESSION.query(User).filter(User.id == id).first()


def searchUserByUsername(username: str):
    return SESSION.query(User).filter(User.username == username).first()


def editUser(user: UserDB):
    user = SESSION.query(User).filter(User.id == user.id).first()
    if not user:
        return False
    user.first_name = user.first_name
    user.last_name = user.last_name
    user.username = user.username
    user.email = user.email
    user.phone = user.phone
    user.address = user.address
    user.town = user.town
    user.created_on = user.created_on
    user.updated_on = user.updated_on
    user.photo = user.photo
    user.is_active = user.is_active
    user.is_admin = user.is_admin
    user.is_staff = user.is_staff
    user.is_superuser = user.is_superuser
    user.is_verified = user.is_verified
    user.is_deleted = user.is_deleted
    user.is_blocked = user.is_blocked
    user.is_suspended = user.is_suspended
    user.is_premium = user.is_premium
    user.is_subscribed = user.is_subscribed
    user.is_trial = user.is_trial
    user.is_trial_used = user.is_trial_used
    user.is_trial_expired = user.is_trial_expired
    SESSION.commit()
    SESSION.close()
    return True


def delete_user(id: int):
    user = SESSION.query(User).filter(User.id == id).first()
    if not user:
        return False
    user.is_deleted = 1
    SESSION.commit()
    SESSION.close()
    return True


def UserToUser(user: UserDB) -> User:
    return User(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        email=user.email,
        phone=user.phone,
        address=user.address,
        town=user.town,
        created_on=user.created_on,
        updated_on=user.updated_on,
        photo=user.photo,
        is_active=user.is_active,
        is_admin=user.is_admin,
        is_staff=user.is_staff,
        is_superuser=user.is_superuser,
        is_verified=user.is_verified,
        is_deleted=user.is_deleted,
        is_blocked=user.is_blocked,
        is_suspended=user.is_suspended,
        is_premium=user.is_premium,
        is_subscribed=user.is_subscribed,
        is_trial=user.is_trial,
        is_trial_used=user.is_trial_used,
        is_trial_expired=user.is_trial_expired,
    )
