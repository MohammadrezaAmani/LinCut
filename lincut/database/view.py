import threading
from lincut.data import SESSION, viewcache
from datetime import datetime, timedelta
from .mainDB import View, User, Link
from lincut.models.view import ViewDB

VIEW_INSERTION_LOCK = threading.RLock()


def add_view_object(view: View):
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


def list_views():
    return SESSION.query(View).all()


def count_views():
    return len(viewcache.views)


def searchviewsByUser(user: User):
    return SESSION.query(View).filter(View.user == user.id).all()


def searchviewById(id: int):
    return SESSION.query(View).filter(View.id == id).first()


def searchviewByLink(link: Link):
    return SESSION.query(View).filter(View.link == link.id).all()


def editview(view: ViewDB):
    view = SESSION.query(View).filter(View.id == view.id).first()
    if not view:
        return False
    view.link = view.link
    view.created_at = view.created_at
    view.id = view.id
    view.ip = view.ip
    view.device = view.device
    view.os = view.os
    view.browser = view.browser
    view.country = view.country
    view.city = view.city
    SESSION.commit()
    SESSION.close()
    return True


def delete_view(id: int):
    view = SESSION.query(View).filter(View.id == id).first()
    if not view:
        return False
    SESSION.delete(view)
    SESSION.commit()
    SESSION.close()
    return True


def viewToview(view: ViewDB) -> View:
    return View(
        link=view.link,
        created_at=view.created_at,
        id=view.id,
        ip=view.ip,
        device=view.device,
        os=view.os,
        browser=view.browser,
        country=view.country,
        city=view.city,
    )
