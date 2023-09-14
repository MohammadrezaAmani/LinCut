from fastapi import APIRouter, HTTPException, responses, Depends
from lincut.database.link import (
    add_link_object,
    count_links,
    delete_link,
    editlink,
    get_link,
    list_links,
    searchlinkById,
    searchlinkBylinkname,
    searchLinkByShortURL,
)
from lincut.models.link import Link, LinkDB, LinkRes
import datetime
from lincut.auth.auth import AuthJWT, getUser
from lincut.models.user import UserLogin
from lincut.database.user import authenicate

router = APIRouter(
    prefix="/api/content",
    tags=["Content"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", response_model=LinkRes)
async def create(data: Link):
    link = LinkDB(
        url=data.url,
        short_url=data.short_url,
        user=0,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
        views=[],
        is_active=1,
        is_deleted=0,
        is_blocked=0,
        reports=0,
    )
    if not add_link_object(link):
        raise HTTPException(status_code=400, detail="Link already exists")
    return LinkRes(
        url=link.url,
        short_url=link.short_url,
        id=link.id,
        created_at=link.created_at,
        views=link.views,
    )


@router.get("/user/create", response_model=LinkRes)
async def create(data: Link, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    user = getUser(Authorize)
    link = LinkDB(
        url=data.url,
        short_url=data.short_url,
        user=user.id,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
        views=[],
        is_active=1,
        is_deleted=0,
        is_blocked=0,
        reports=0,
    )
    if not add_link_object(link):
        raise HTTPException(status_code=400, detail="Link already exists")
    return LinkRes(
        url=link.url,
        short_url=link.short_url,
        id=link.id,
        created_at=link.created_at,
        views=link.views,
    )


@router.get("/list", response_model=list[LinkRes])
async def list(Auth: AuthJWT = Depends()):
    Auth.jwt_required()
    user = getUser(Auth)
    if user.is_admin:
        return list_links()
    else:
        return searchlinkBylinkname(user.username)


@router.get("/user/list", response_model=list[LinkRes])
async def list(Auth: AuthJWT = Depends()):
    Auth.jwt_required()
    user = getUser(Auth)
    return searchlinkBylinkname(user.username)


@router.get("/count", response_model=int)
async def count(Auth: AuthJWT = Depends()):
    Auth.jwt_required()
    user = getUser(Auth)
    if user.is_admin:
        return count_links()
    else:
        return len(searchlinkBylinkname(user.username))


@router.get("/get/{id}", response_model=LinkRes)
async def get(id: int):
    link = searchlinkById(id)
    if not link:
        raise HTTPException(status_code=400, detail="Link not found")
    return LinkRes(
        url=link.url,
        short_url=link.short_url,
        id=link.id,
        created_at=link.created_at,
        views=link.views,
    )


@router.get("/user/get/{id}", response_model=LinkDB)
async def get(id: int, Auth: AuthJWT = Depends()):
    Auth.jwt_required()
    user = getUser(Auth)
    link = searchlinkById(id)
    if not link:
        raise HTTPException(status_code=400, detail="Link not found")
    if link.user != user.id:
        raise HTTPException(status_code=400, detail="Link not found")
    return link


@router.put("/user/edit/{id}", response_model=LinkDB)
async def edit(id: int, data: Link, Auth: AuthJWT = Depends()):
    Auth.jwt_required()
    user = getUser(Auth)
    link = searchlinkById(id)
    if not link:
        raise HTTPException(status_code=400, detail="Link not found")
    if link.user != user.id:
        raise HTTPException(status_code=400, detail="Link not found")
    link.url = data.url
    link.short_url = data.short_url
    link.updated_at = datetime.datetime.now()
    if not editlink(link):
        raise HTTPException(status_code=400, detail="Link not found")
    return link


@router.delete("/user/delete/{id}")
async def delete(id: int, Auth: AuthJWT = Depends()):
    Auth.jwt_required()
    user = getUser(Auth)
    link = searchlinkById(id)
    if not link:
        raise HTTPException(status_code=400, detail="Link not found")
    if link.user != user.id:
        raise HTTPException(status_code=400, detail="Link not found")
    if not delete_link(id):
        raise HTTPException(status_code=400, detail="Link not found")
    return responses.RedirectResponse(url="/user/dashboard")
