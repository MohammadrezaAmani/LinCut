from fastapi import APIRouter, Depends, HTTPException
from lincut import DB
from lincut.models.token import RefreshToken, Token
from lincut.auth.auth import AuthJWT, getUser
from lincut.models.user import UserLogin

router = APIRouter(
    tags=["Token"],
    responses={404: {"description": "Not found"}},
)


@router.post("/refresh")
def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return RefreshToken(access_token=new_access_token)


@router.post("/token")
def login(user: UserLogin, Authorize: AuthJWT = Depends()):
    userInDB = DB.authenicate(user.email, user.password)
    if not userInDB:
        raise HTTPException(status_code=401, detail="Bad email or password")

    access_token = Authorize.create_access_token(subject=user.email)
    refresh_token = Authorize.create_refresh_token(subject=user.email)
    return Token(access_token=access_token, refresh_token=refresh_token)
