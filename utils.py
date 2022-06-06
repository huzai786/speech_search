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
    
speak("I want a script that will run in the background and when i press certain keys combination, that bot get activated with \
    the bot saying 'activated'then to search a meaning, i have to say 'search <word>', and it will open that word on google and \
        after 5 sec, it will close automatically and i'll drop to the main page, where i was before.")
