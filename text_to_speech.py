from gtts import gTTS
import os

def speech_conversion(mytext):
    language = 'en'
    speech = gTTS(text=mytext, lang = language, slow=False)
    speech.save("speech.mp3")
    os.system("speech.mp3")

