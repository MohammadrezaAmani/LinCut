from fastapi import APIRouter, Depends, HTTPException
from lincut.models.token import RefreshToken, Token
from lincut.auth.auth import AuthJWT, getUser
from lincut.models.user import UserLogin
from lincut.database.user import authenicate

router = APIRouter(
    tags=["Token"],
    responses={404: {"description": "Not found"}},
)


@router.post("/refresh", response_model=RefreshToken)
async def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return RefreshToken(access_token=new_access_token)


@router.post("/token", response_model=Token)
async def login(user: UserLogin, Authorize: AuthJWT = Depends()):
    userInDB = authenicate(user.email, user.password)
    if not userInDB:
        raise HTTPException(status_code=401, detail="Bad email or password")

    access_token = Authorize.create_access_token(subject=user.email)
    refresh_token = Authorize.create_refresh_token(subject=user.email)
    return Token(access_token=access_token, refresh_token=refresh_token)
