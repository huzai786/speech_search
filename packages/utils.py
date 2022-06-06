import speech_recognition as sr
import os
import time
import pyaudio
from gtts import gTTS
from playsound import playsound


def speak(text):
    tts = gTTS(text, lang='en')
    tts.save('text.mp3')
    playsound('text.mp3')
    os.remove('text.mp3')
    
def get_audio():
    try:
        r = sr.Recognizer()
        said = ""
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            said = r.recognize_google(audio)
    except sr.UnknownValueError:
        said = "sorry i could not understand your voice"
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    return said