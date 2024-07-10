import os
import time

import pyttsx3
from gtts import gTTS
from playsound import playsound

def Voice(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save("voice.mp3")
        playsound("voice.mp3", block=True) # play sound

        time.sleep(1)

        os.remove("voice.mp3") # delete after
    except Exception as e:
        print(f"Error {e}")
