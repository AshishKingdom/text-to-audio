import requests
import base64
import zlib
url = "https://775b-2409-40d0-100c-3df-3ed5-44bc-fe8b-2a8.ngrok-free.app/text_to_audio"
data = {
  "count": 1,
  "texts": [
    {
      "text": "This is an example string",
      "voice_gender": "Female"
    }
  ]
}
response = requests.post(url,
                          json=data, 
                          headers={"Content-Type": "application/json",
                                   "ngrok-skip-browser-warning":"huehuehue"}
                          )

if response.status_code==200:
    audio_data = response.json()["audio"][0]["data"]
    print(audio_data)
    audio_bytes = base64.b64decode(audio_data)
    decompressed_audio = zlib.decompress(audio_bytes)
    with open("audio.mp3", "wb") as f:
        f.write(decompressed_audio)
    
else:
    print("Error")