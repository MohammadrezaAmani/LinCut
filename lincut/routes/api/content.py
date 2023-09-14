from fastapi import APIRouter, HTTPException, responses
from lincut import DB
from lincut.models.link import Link, LinkDB, LinkRes
import datetime

router = APIRouter(
    prefix="/api/content",
    tags=["Content"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", response_model=LinkRes)
async def create(data: Link):
    print(data)
    id = len(DB.LinksDB) + 1
    is_succes = DB.addLink(
        LinkDB(
            id=id,
            url=data.url,
            short_url=data.short_url,
            user_id=1,
            created_at=str(datetime.datetime.now()),
            updated_at=str(datetime.datetime.now()),
            views=1,
        )
    )
    if is_succes:
        return LinkRes(
            id=id,
            url=data.url,
            short_url=data.short_url,
            views=is_succes.views,
            created_at=is_succes.created_at,
        )
    else:
        raise HTTPException(status_code=400, detail="bad short link")


@router.get("/get/{short_url}", response_model=LinkRes)
async def get(short_url: str):
    data = DB.searchLinkByShortUrl(short_url)
    if data:
        DB.addView(data.id)
        return LinkRes(
            id=data.id,
            url=data.url,
            short_url=data.short_url,
            views=data.views,
            created_at=data.created_at,
        )
    else:
        raise HTTPException(status_code=404, detail="Not found")


@router.get("/getid/{id}", response_model=LinkRes)
async def get(id: int):
    data = DB.searchLink(id)
    if data:
        DB.addView(data.id)
        return LinkRes(
            id=data.id,
            url=data.url,
            short_url=data.short_url,
            views=data.views,
            created_at=data.created_at,
        )
    else:
        raise HTTPException(status_code=404, detail="Not found")
