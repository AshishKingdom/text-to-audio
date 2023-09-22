import requests
import base64
import zlib
url = "http://localhost:4000/text_to_audio"
data = {
  "count": 1,
  "texts": [
    {
      "text": "This is an example string. It is only being used for testing purpose and nothing else.",
      "voice_gender": "Female",
      "language": "English"
    }
  ]
}
response = requests.post(url,
                          json=data, 
                          headers={"Content-Type": "application/json",
                                   "ngrok-skip-browser-warning":"huehuehue"}
                          )

if response.status_code==200:
    print("Audio response received from azure")
    audio_data = response.json()["audio"][0]["data"]
    audio_bytes = base64.b64decode(audio_data)
    decompressed_audio = zlib.decompress(audio_bytes)
    with open("audio.mp3", "wb") as f:
        f.write(decompressed_audio)
    
else:
    print("Error")