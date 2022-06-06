import speech_recognition as sr
import os
import time
import pyaudio
from gtts import gTTs


r = sr.Recognizer()



while True:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.8)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            
    except Exception as e:
        print(e)


