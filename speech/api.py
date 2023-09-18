import requests
from settings import Settings


def azure_text_to_audio(text:str, access_token:str, gender:str="Female")->bytes:
    """Convert text to audio"""

    api_headers = {
        "Ocp-Apim-Subscription-Key": Settings.SPEECH_KEY,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-16khz-32kbitrate-mono-mp3",#"ogg-16khz-16bit-mono-opus",
        "User-Agent": "python-script",
        "Authorization": f"Bearer {access_token}"
    }

    #"en-US-JennyNeural",#
    if gender.lower()=="male":
        voice_actor_name = "hi-IN-MadhurNeural"
    else:
        voice_actor_name = "hi-IN-SwaraNeural"
    
    speech_config = {
        "version":"1.0",
        "xml:lang":"en-US",
        "xml:gender":gender,
        "name": voice_actor_name,
        "data":text
    }

    payload = f"""
                <speak version='{speech_config['version']}' xml:lang='{speech_config['xml:lang']}'>
                    <voice xml:lang='{speech_config['xml:lang']}' xml:gender='{speech_config['xml:gender']}' name='{speech_config['name']}'>
                        <prosody rate="+15%">
                                {speech_config['data']}
                        </prosody>
                    </voice>
                </speak>
                """
    
    response = requests.post(f"https://{Settings.SPEECH_REGION}.tts.speech.microsoft.com/cognitiveservices/v1",
                            headers=api_headers,
                            data=payload
                            )
    
    if response.status_code==200:
        return response.content
    else:
        raise Exception("Failed to convert text to audio ", response.status_code, response.text)
