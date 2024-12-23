import logging
import sys
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.api.controllers.user_controller import UserController
from src.infrastructure.database import sessionmanager
from src.infrastructure.settings import settings

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG if settings.debug_logs else logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """
    yield
    if sessionmanager._engine is not None:
        # Close the DB connection
        await sessionmanager.close()


app = FastAPI(lifespan=lifespan, title=settings.project_name, version='1.0')


@app.get("/")
async def root():
    return {'message': 'Welcome to VisualStory!'}


app.include_router(UserController().router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
