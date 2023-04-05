# modules imports
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")  # search for html files inside the templates folder


general_pages_router = APIRouter() # instance of the api router

# capture the actual request and return an HTMLResponse 
@general_pages_router.get("/")
async def home(request: Request):
	return templates.TemplateResponse("general_pages/homepage.html",{"request":request})