from fastapi import APIRouter, HTTPException, status, Depends
from schemas.text import TextToAudioBody, TextToAudioResponse
from speech.token_generation import get_access_token
from speech.api import azure_text_to_audio

import soundfile as sf
from io import BytesIO
import base64, zlib

router = APIRouter()

@router.post("/text_to_audio", response_model=TextToAudioResponse, tags=["text_to_audio"])
def text_to_audio(body:TextToAudioBody, access_token:str=Depends(get_access_token))->TextToAudioResponse:
    """
    Convert text to audio
    """

    if body.count==0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Count cannot be zero")
    
    audio_list = []
    total_duration:int = 0
    for text_info in body.texts:
        try:
            print("text = ",text_info.text)
            audio = azure_text_to_audio(text_info.text, access_token,text_info.language, text_info.voice_gender)
            if len(audio)==0:
                print("No Audio returned from azure")
                continue
            compressed_audio = zlib.compress(audio)
            print("Audio Compressed")
            compressed_audio_data = base64.b64encode(compressed_audio).decode("utf-8")
            print("Audio Encoded to base64")
            print("Audio Data = \n ", compressed_audio_data)
            print("------------------------------------")
            print("Reading Audio to get duration")
            ogg_audio, sample_rate = sf.read(BytesIO(audio))
            duration:int = len(ogg_audio)//sample_rate
            print("Audio Duration = ", duration, " seconds")
            audio_list.append({
                "duration": duration,
                "data": compressed_audio_data
            })
            total_duration += duration
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                 detail="some error occured during batch conversion of audio")
    
    return TextToAudioResponse(audio=audio_list, status="success", total_duration=total_duration)