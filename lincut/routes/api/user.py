from fastapi import APIRouter, HTTPException, Depends
from lincut.auth.auth import AuthJWT, getUser
from lincut.models.user import (
    UserLogin,
    UserSchema,
    UserSignUp,
    UserInDBSchema,
)
from lincut.models.token import Settings, Token
from lincut import DB

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login")
def login(user: UserLogin, Authorize: AuthJWT = Depends()):
    userInDB = DB.authenicate(user.email, user.password)
    if not userInDB:
        raise HTTPException(status_code=401, detail="Bad email or password")

    access_token = Authorize.create_access_token(subject=user.email)
    refresh_token = Authorize.create_refresh_token(subject=user.email)
    return Token(access_token=access_token, refresh_token=refresh_token)


@router.get("/protected")
def protected(Authorize: AuthJWT = Depends()):
    user = getUser(Authorize)
    return UserSchema(
        id=user.id,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        phone_number=user.phone_number,
        address=user.address,
        city=user.city,
        state=user.state,
        country=user.country,
        gender=user.gender,
        date_of_birth=user.date_of_birth,
    )


@router.post("/signup")
def protected(user_data: UserSignUp):
    UserInDB = UserInDBSchema(
        id=len(DB.PatientUsersDB) + 1,
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        phone_number=user_data.phone,
        password=user_data.password,
    )
    DB.addPatientUser(UserInDB)
    Auth = AuthJWT()
    access_token = Auth.create_access_token(subject=UserInDB.email)
    refresh_token = Auth.create_refresh_token(subject=UserInDB.email)
    return Token(access_token=access_token, refresh_token=refresh_token)


@router.get("/{user_id}")
async def searchUser(user_id: int, Authorize: AuthJWT = Depends()):
    return UserSchema(**DB.searchUser(user_id).dict())


@router.put("/")
async def editUser(user: UserInDBSchema, Authorize: AuthJWT = Depends()):
    return UserSchema(**DB.editUser(user).dict())


@router.delete("/{user_id}")
async def deleteUser(user_id: int, Authorize: AuthJWT = Depends()):
    return DB.deleteUser(user_id)


@router.get("/logout")
async def logout(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    Authorize.unset_jwt_cookies()
    return {"msg": "Successfully logout"}


@router.get("/me")
async def me(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return UserSchema(**getUser(Authorize).dict())


@router.get("/mypatients")
async def drpatients(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return UserSchema(**getUser(Authorize).dict())
