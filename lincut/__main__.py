from .config import Config
from fastapi import FastAPI
from .routes.api.content import router as contentRouter

if __name__ == "__main__":
    app = FastAPI()
    app.include_router(contentRouter)
    import uvicorn

    uvicorn.run(app, host=Config.IP, port=Config.PORT)
