from fastapi_jwt_auth import AuthJWT
from lincut.models.token import Settings
from lincut import DB


@AuthJWT.load_config
def get_config():
    return Settings()


def getUser(Authorize: AuthJWT):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    return DB.searchUserByEmail(current_user)
