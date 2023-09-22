import requests
from settings import Settings

def get_access_token()->str:
    """Get access token for speech api"""
    response = requests.post(f"https://{Settings.SPEECH_REGION}.api.cognitive.microsoft.com/sts/v1.0/issuetoken",
                             headers={"Ocp-Apim-Subscription-Key":Settings.SPEECH_KEY}
                             )
    if response.status_code==200:
        print("access token granted")
        return response.text
    else:
        raise Exception("Failed to get access token for speech api", response.status_code, response.text)