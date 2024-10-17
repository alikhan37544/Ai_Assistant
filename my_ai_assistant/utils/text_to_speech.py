import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()
