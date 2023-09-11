from .config import Config
from fastapi import FastAPI

if __name__ == "__main__":
    app = FastAPI()

    # app.include_router(user.router)

    # @app.exception_handler(AuthJWTException)
    # def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    #     return JSONResponse(
    #         status_code=exc.status_code, content={"detail": exc.message}
    #     )

    @app.get("/")
    async def root():
        return {"message": "hello world!"}

    import uvicorn

    uvicorn.run(app, host=Config.IP, port=Config.PORT)
