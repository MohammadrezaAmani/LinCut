from .config import Config
from fastapi import FastAPI
from .routes.api.content import router as contentRouter
from .routes.api.user import router as userRouter
from .routes.api.token import router as tokenRouter

if __name__ == "__main__":
    app = FastAPI()
    app.include_router(contentRouter)
    app.include_router(userRouter)
    app.include_router(tokenRouter)
    import uvicorn

    uvicorn.run(app, host=Config.IP, port=Config.PORT)
