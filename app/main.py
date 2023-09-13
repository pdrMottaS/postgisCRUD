from fastapi import FastAPI
from app.controller import testController

from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(testController.router)
