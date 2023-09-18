from pydantic import BaseModel
from typing import List
# import hashlib

class TextInfo(BaseModel):
    """
    Single Text Info for text to audio
    """
    text:str
    voice_gender:str


class TextToAudioBody(BaseModel):
    """
    Body for text to audio request
    """
    count:int
    texts:List[TextInfo]


class AudioInfo(BaseModel):
    """
    Single audio info for text to audio response
    """
    # filename:str|None
    # url:str|None
    duration:int
    data:str


class TextToAudioResponse(BaseModel):
    """
    Response for text to audio request
    """
    audio:List[AudioInfo]
    status:str
    total_duration:int