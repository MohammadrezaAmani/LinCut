import threading
from lincut.data import SESSION, viewcache
from datetime import datetime, timedelta
from .mainDB import view, View
from lincut.models.view import viewDB

VIEW_INSERTION_LOCK = threading.RLock()


def add_view(id: int):
    with VIEW_INSERTION_LOCK:
        view = SESSION.query(View).filter(View.id == id).first()
        if view:
            SESSION.expunge(view)
            SESSION.close()
            return view
        view = view(id)
        viewcache.add_view(view)
        print(f"added view: {str(view)}")
        SESSION.add(view)
        SESSION.commit()
        SESSION.close()
        return view


def add_view_object(view: view):
    with VIEW_INSERTION_LOCK:
        prev_view = SESSION.query(View).filter(View.id == view.id).first()
        if prev_view:
            SESSION.close()
            return False
        view = viewToview(view)
        SESSION.add(view)
        SESSION.commit()
        SESSION.close()
        return True


def get_view(id: int):
    return SESSION.query(View).filter(View.id == id).first()


def count_active_views(minutes: int):
    return (
        SESSION.query(View)
        .filter(view.last_active >= datetime.utcnow() - timedelta(minutes=minutes))
        .count()
    )


def count_new_signups(minutes: int):
    return (
        SESSION.query(View)
        .filter(view.signup_date >= datetime.utcnow() - timedelta(minutes=minutes))
        .count()
    )


def list_views():
    return SESSION.query(View).all()


def count_views():
    return len(viewcache.views)


def authenicate(email: str, password: str):
    return (
        SESSION.query(View)
        .filter(view.email == email, view.password == password)
        .first()
    )


def searchviewByEmail(email: str):
    return SESSION.query(View).filter(view.email == email).first()


def searchviewById(id: int):
    return SESSION.query(View).filter(View.id == id).first()


def searchviewByviewname(viewname: str):
    return SESSION.query(View).filter(view.viewname == viewname).first()


def editview(view: viewDB):
    view = SESSION.query(View).filter(View.id == view.id).first()
    if not view:
        return False
    view.first_name = view.first_name
    view.last_name = view.last_name
    view.viewname = view.viewname
    view.email = view.email
    view.phone = view.phone
    view.address = view.address
    view.town = view.town
    view.created_on = view.created_on
    view.updated_on = view.updated_on
    view.photo = view.photo
    view.is_active = view.is_active
    view.is_admin = view.is_admin
    view.is_staff = view.is_staff
    view.is_superview = view.is_superview
    view.is_verified = view.is_verified
    view.is_deleted = view.is_deleted
    view.is_blocked = view.is_blocked
    view.is_suspended = view.is_suspended
    view.is_premium = view.is_premium
    view.is_subscribed = view.is_subscribed
    view.is_trial = view.is_trial
    view.is_trial_used = view.is_trial_used
    view.is_trial_expired = view.is_trial_expired
    SESSION.commit()
    SESSION.close()
    return True


def delete_view(id: int):
    view = SESSION.query(View).filter(View.id == id).first()
    if not view:
        return False
    view.is_deleted = 1
    SESSION.commit()
    SESSION.close()
    return True


def viewToview(view: viewDB) -> view:
    return view(
        id=view.id,
        first_name=view.first_name,
        last_name=view.last_name,
        viewname=view.viewname,
        email=view.email,
        phone=view.phone,
        address=view.address,
        town=view.town,
        created_on=view.created_on,
        updated_on=view.updated_on,
        photo=view.photo,
        is_active=view.is_active,
        is_admin=view.is_admin,
        is_staff=view.is_staff,
        is_superview=view.is_superview,
        is_verified=view.is_verified,
        is_deleted=view.is_deleted,
        is_blocked=view.is_blocked,
        is_suspended=view.is_suspended,
        is_premium=view.is_premium,
        is_subscribed=view.is_subscribed,
        is_trial=view.is_trial,
        is_trial_used=view.is_trial_used,
        is_trial_expired=view.is_trial_expired,
    )
