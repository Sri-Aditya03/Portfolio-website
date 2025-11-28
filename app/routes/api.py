from fastapi import APIRouter
from app.data.projects import PROJECTS

api_router = APIRouter()

@api_router.get("/projects")
def get_projects():
    return PROJECTS
