import logging
import sys
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from src.api.controllers.post_controller import PostController
from src.api.routes import router
from src.api.controllers.authentication_controller import AuthenticationController
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


# General Setups
app = FastAPI(lifespan=lifespan, title=settings.project_name, version='1.0')
app.mount("/static", StaticFiles(directory="src/ui/static"), name="static")

# Route Setups
app.include_router(router)
app.include_router(UserController().router)
app.include_router(AuthenticationController().router)
app.include_router(PostController().router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
