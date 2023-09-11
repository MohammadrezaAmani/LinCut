from fastapi import APIRouter, HTTPException, responses
from lincut import DB
from lincut.models.content import Link, LinkDB
import datetime

router = APIRouter(
    prefix="/api/content",
    tags=["Token"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create")
def create(data: Link):
    DB.addLink(
        LinkDB(
            id=len(DB.LinksDB) + 1,
            url=data.url,
            short_url=data.short_url,
            user_id=1,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            deleted_at=None,
        )
    )
    return data


@router.get("/{short_url}")
def get(short_url: str):
    data = DB.searchLinkByShortUrl(short_url)
    if data:
        return responses.RedirectResponse(data.url)
    else:
        raise HTTPException(status_code=404, detail="Not found")
