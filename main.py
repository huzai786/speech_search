from pynput import keyboard
import requests 
import webbrowser
from packages.utils import (
    speak,
    get_audio
)


def voice_search():
    speak('initiated')
    text = get_audio()
    if 'search' in text:
        word = text.replace('search', '')
        print(f'searching {word}')
        speak(f'searching {word}')
        webbrowser.open(f'https://www.google.com/search?q={word}')
    if "hello" in text:
        speak('Hi welcome to your voice assistant, how can i help you')
    if 'what is your name' in text:
        speak("my name is alexa don't you know?")


def on_press(key):
    if key == keyboard.Key.esc:
        return True
    try:
        k = key.char
    except:
        k = key.name
    if k in ['1', '2', 'left']:
        print(k)
        voice_search()
        return False



while True:
    listener = keyboard.Listener(on_press = on_press)
    listener.start()
    listener.join()

