from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

page_router = APIRouter()

@page_router.get("/")
def home(request: Request):
    return templates.TemplateResponse(request=request, name="home.html", context={"request": request})

@page_router.get("/about")
def about(request: Request):
    return templates.TemplateResponse(request=request, name="about.html", context={"request": request})

@page_router.get("/experience")
def experience(request: Request):
    return templates.TemplateResponse(request=request, name="experience.html", context={"request": request})

@page_router.get("/projects")
def projects(request: Request):
    return templates.TemplateResponse(request=request, name="projects.html", context={"request": request})

@page_router.get("/contact")
def contact(request: Request):
    return templates.TemplateResponse(request=request, name="contact.html", context={"request": request})

@page_router.get("/resume")
def resume(request: Request):
    return templates.TemplateResponse(request=request, name="resume.html", context={"request": request})

