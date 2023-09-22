from pydantic import BaseModel
from typing import List
# import hashlib


class TextInfo(BaseModel):
    """
    Single Text Info for text to audio
    """
    text:str = "This is a test string"
    voice_gender:str = "female"
    language:str = "english"
    style:str = "documentary-narration"
    speed:str = "+0.00%" 


class TextToAudioBody(BaseModel):
    """
    Body for text to audio request
    """
    count:int=1
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