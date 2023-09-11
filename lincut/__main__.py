from .config import Config
from fastapi import FastAPI, Request
from .routes.api.user import router as user
from .routes.api.token import router as token

from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.responses import JSONResponse

if __name__ == "__main__":
    app = FastAPI()

    app.include_router(user)
    app.include_router(token)

    @app.exception_handler(AuthJWTException)
    def authjwt_exception_handler(request: Request, exc: AuthJWTException):
        return JSONResponse(
            status_code=exc.status_code, content={"detail": exc.message}
        )

    @app.get("/")
    async def root():
        return {"message": "hello world!"}

    import uvicorn

    uvicorn.run(app, host=Config.IP, port=Config.PORT)
