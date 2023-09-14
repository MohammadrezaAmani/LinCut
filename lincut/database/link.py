import threading
from lincut.data import SESSION
from datetime import datetime, timedelta
from .mainDB import User, View, Link
from lincut.models.link import LinkDB

LINK_INSERTION_LOCK = threading.RLock()


def add_link_object(link: LinkDB):
    with LINK_INSERTION_LOCK:
        prev_link = SESSION.query(Link).filter(Link.id == link.id).first()
        if prev_link:
            SESSION.close()
            return False
        link = linkTolink(link)
        SESSION.add(link)
        SESSION.commit()
        SESSION.close()
        return True


def get_link(id: int):
    return SESSION.query(Link).filter(Link.id == id).first()


def list_links():
    return SESSION.query(Link).all()


def count_links():
    return SESSION.query(Link).count()


def searchLinkByShortURL(short_url: str):
    return SESSION.query(Link).filter(Link.short_url == short_url).first()


def searchlinkById(id: int):
    return SESSION.query(Link).filter(Link.id == id).first()


def searchlinkBylinkname(url: str):
    return SESSION.query(Link).filter(Link.url == url).first()


def editlink(link: LinkDB):
    link = SESSION.query(Link).filter(Link.id == link.id).first()
    if not link:
        return False
    link.url = link.url
    link.short_url = link.short_url
    link.user = link.user
    link.created_at = link.created_at
    link.updated_at = link.updated_at
    link.views = link.views
    link.is_active = link.is_active
    link.is_deleted = link.is_deleted
    link.is_blocked = link.is_blocked
    link.reports = link.reports
    SESSION.commit()
    SESSION.close()
    return True


def delete_link(id: int):
    link = SESSION.query(Link).filter(Link.id == id).first()
    if not link:
        return False
    SESSION.delete(link)
    SESSION.commit()
    SESSION.close()
    return True


def linkTolink(link: LinkDB) -> Link:
    return Link(
        id=link.id,
        url=link.url,
        short_url=link.short_url,
        user=link.user,
        created_at=link.created_at,
        updated_at=link.updated_at,
        views=link.views,
        is_active=link.is_active,
        is_deleted=link.is_deleted,
        is_blocked=link.is_blocked,
        reports=link.reports,
    )
