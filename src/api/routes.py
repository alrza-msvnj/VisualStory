from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="src/ui/templates")

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse(
#         request=request, name="item.html", context={"id": id}
#     )

@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


@router.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse(request=request, name="register.html")


@router.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    return templates.TemplateResponse(request=request, name="profile.html")
