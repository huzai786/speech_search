import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

# with sr.Microphone() as source:
#     print('say something!')
#     audio = r.listen(source)
#     sr.adjust_for_ambient_noise(source)
#     voice_data = r.recognize_google(audio)
#     print(voice_data)
    

while True:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.8)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            
    except Exception as e:
        print(e)
        