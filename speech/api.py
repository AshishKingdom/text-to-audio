import requests
from settings import Settings
from language_models import language_models, language_mapping


def azure_text_to_audio(text:str, access_token:str, lang:str="english", gender:str="Female", style:str="documentary-narration", speed:str="+0.00%")->bytes:
    """Convert text to audio"""

    api_headers = {
        "Ocp-Apim-Subscription-Key": Settings.SPEECH_KEY,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-16khz-32kbitrate-mono-mp3",#"ogg-16khz-16bit-mono-opus",
        "User-Agent": "python-script",
        "Authorization": f"Bearer {access_token}"
    }

    lang = language_mapping[lang.lower()]
    print("Voice Style = ", style)

    if gender.lower()=="male":
        role = "SeniorMale"
        voice_actor_name = language_models[lang]['male']
    else:
        role = "SeniorFemale"
        voice_actor_name = language_models[lang]['female']

    print("Voice Role = ", role)
    print('voice_actor_name : ', voice_actor_name)

    speech_config = {
        "version":"1.0",
        "xmlns":"https://www.w3.org/2001/10/synthesis",
        "xmlns:mstts":"https://www.w3.org/2001/mstts",
        "xml:lang":lang,
        "xml:gender":gender,
        "name": voice_actor_name,
        "data":text
    }

    payload = f"""
                <speak version='{speech_config['version']}' xml:lang='{speech_config['xml:lang']}' xmlns='{speech_config['xmlns']}' xmlns:mstts='{speech_config['xmlns:mstts']}'>
                    <voice xml:gender='{speech_config['xml:gender']}' name='{speech_config['name']}'>
                            <mstts:express-as style="{style}" styledegree='2' role='{role}'>
                                <prosody rate='{speed}'>
                                    <lang xml:lang='{lang}'>
                                        {speech_config['data']}
                                    </lang>
                                </prosody>
                            </mstts:express-as>
                    </voice>
                </speak>
                """
    print("payload \n ", payload)
    print("----------------------------------")
    response = requests.post(f"https://{Settings.SPEECH_REGION}.tts.speech.microsoft.com/cognitiveservices/v1",
                            headers=api_headers,
                            data=payload.encode("utf-8")
                            )
    
    if response.status_code==200:
        print("Audio response received from azure")
        return response.content
    else:
        raise Exception("Failed to convert text to audio ", response.status_code, response.text)
