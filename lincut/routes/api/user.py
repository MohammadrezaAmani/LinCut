from fastapi import APIRouter, Depends, HTTPException
from lincut.models.token import Token
from lincut.auth.auth import AuthJWT, getUser
from lincut.models.user import UserLogin
from lincut.database.user import authenicate
from lincut.database.user import (
    add_user_object,
    authenicate,
    count_active_users,
    count_new_signups,
    count_users,
    get_user,
    list_users,
    searchUserByEmail,
    datetime,
    searchUserByUsername,
    editUser,
    delete_user,
)
from lincut.models.user import User, UserDB, UserLogin, UserSignUp

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.post("/signup", response_model=Token)
async def signup(user: UserSignUp, Authorize: AuthJWT = Depends()):
    if searchUserByEmail(user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if searchUserByUsername(user.username):
        raise HTTPException(
            status_code=400, detail="Username already registered")
    user = UserDB(
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        email=user.email,
        phone=user.phone,
        address=user.address,
        town=user.town,
        photo=user.photo,
        password=user.password,
        created_on=(datetime.utcnow()),
        updated_on=(datetime.utcnow()),
        is_active=1,
        is_admin=0,
        is_staff=0,
        is_superuser=0,
        is_verified=0,
        is_deleted=0,
        is_blocked=0,
        is_suspended=0,
        is_premium=0,
        is_subscribed=0,
        is_trial=0,
        is_trial_used=0,
        is_trial_expired=0,
        id=count_users()+1,
    )
    user = add_user_object(user)
    if user:
        access_token = Authorize.create_access_token(subject=user.email)
        refresh_token = Authorize.create_refresh_token(subject=user.email)
        return Token(access_token=access_token, refresh_token=refresh_token)
    else:
        return HTTPException(status_code=401, detail="Bad email or password")


@router.post("/login", response_model=Token)
async def login(user: UserLogin, Authorize: AuthJWT = Depends()):
    userInDB = authenicate(user.email, user.password)
    if not userInDB:
        raise HTTPException(status_code=401, detail="Bad email or password")

    access_token = Authorize.create_access_token(subject=user.email)
    refresh_token = Authorize.create_refresh_token(subject=user.email)
    return Token(access_token=access_token, refresh_token=refresh_token)


@router.get("/me", response_model=User)
async def me(Authorize: AuthJWT = Depends()):
    user = getUser(Authorize)
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


@router.get("/count")
async def count():
    return count_users()


@router.get("/list", response_model=list[User])
async def list(Authorize: AuthJWT = Depends()):
    AuthJWT.jwt_required()
    return list_users()


@router.get("/count/active")
async def count_active(minutes: int, Authorize: AuthJWT = Depends()):
    AuthJWT.jwt_required()
    return count_active_users(minutes)


@router.get("/count/new")
async def count_new(minutes: int, Authorize: AuthJWT = Depends()):
    AuthJWT.jwt_required()
    return count_new_signups(minutes)


@router.get("/get/{id}", response_model=User)
async def get(id: int, Authorize: AuthJWT = Depends()):
    AuthJWT.jwt_required()
    return get_user(id)


@router.get("/search/email/{email}", response_model=User)
async def search_email(email: str, Authorize: AuthJWT = Depends()):
    AuthJWT.jwt_required()
    return searchUserByEmail(email)


@router.get("/search/username/{username}", response_model=User)
async def search_username(username: str, Authorize: AuthJWT = Depends()):
    AuthJWT.jwt_required()
    return searchUserByUsername(username)


@router.delete("/delete")
async def delete(Authorize: AuthJWT = Depends()):
    AuthJWT.jwt_required()
    user = getUser(Authorize)
    return delete_user(user.id)


@router.put("/edit")
async def edit(user: UserDB, Authorize: AuthJWT = Depends()):
    AuthJWT.jwt_required()
    return editUser(user)
