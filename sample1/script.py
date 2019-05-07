import aiml
import os
import time,sys
import pyttsx
import warnings
import speech_recognition as sr
import pyaudio
import os
terminate=['bye','shutdown','exit','quit','gotosleep','goodbye']

def offline_speak(voice_of_jarvis):
    # engine = pyttsx.init()
    # engine.setProperty('rate',150)
    # engine.say(voice_of_jarvis)
    # engine.runAndWait()
    os.system("say "+voice_of_jarvis)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
    with sr.Microphone() as source:
        print("Talk to JARVIS")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        offline_speak("Sorry I cannot understand , can you say it again")
        return(listen())
    except sr.RequestError as e:
        print("Could not get results")

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands="load aiml b")
    kernel.saveBrain("bot_brain.brn")

while True:
    response = listen()
    if response.lower().replace(" "," ") in terminate:
        break
    jarvis_speech = kernel.respond(response)
    offline_speak(jarvis_speech)
