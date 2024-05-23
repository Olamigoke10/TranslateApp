import pyttsx3

def Voice(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()