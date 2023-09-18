from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    SPEECH_REGION = os.getenv("SPEECH_REGION")
    SPEECH_KEY = os.getenv("SPEECH_KEY")