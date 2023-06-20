import os

from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse, HTMLResponse

demo_route = APIRouter()
templates = Jinja2Templates(os.path.join(os.path.dirname(__file__)))
path1 = os.path.join(os.path.dirname(__file__))
@demo_route.get("/", include_in_schema=False)
async def home_doc(req: Request) -> HTMLResponse:
	return templates.TemplateResponse('index.html', {"request": req})

