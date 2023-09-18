import requests
from settings import Settings

def get_access_token()->str:
    """Get access token for speech api"""
    response = requests.post(f"https://{Settings.SPEECH_REGION}.api.cognitive.microsoft.com/sts/v1.0/issuetoken",
                             headers={"Ocp-Apim-Subscription-Key":Settings.SPEECH_KEY}
                             )
    return response.text