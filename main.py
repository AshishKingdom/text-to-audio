from fastapi import FastAPI
from base import base_router

app = FastAPI()
app.include_router(base_router)

