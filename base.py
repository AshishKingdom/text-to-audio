from api import text_to_audio
from fastapi import APIRouter

base_router = APIRouter()
base_router.include_router(text_to_audio.router)