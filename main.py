from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.pages import page_router
from app.routes.api import api_router

app = FastAPI(title="Aditya Portfolio")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Routers
app.include_router(page_router)
app.include_router(api_router, prefix="/api")
