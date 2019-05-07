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
    query = response.lower().split(" ")
    if response.lower().replace(" "," ") in terminate:
        break
    elif response.lower() == "hello jarvis" :
        os.system("say sir how may i help you")
    elif response.lower() == "open safari" :
        os.system("open -a safari")
        os.system("say opening safari browser")
    elif response.lower() == "open itunes" :
        os.system("open -a itunes")
        os.system("say opening itunes")
    elif response.lower() == "open calculator" :
        os.system("open -a calculator")
        os.system("say opening calculator")
    elif response.lower() == "open chrome" :
        os.system("open -a chrome")
        os.system("say opening chrome browser")
    elif response.lower() == "who are you" :
        os.system("say I am Mark42")
    elif response.lower() == "open google" :
        os.system("say opening google")
        os.system("open -a safari 'https://www.google.com'")
    elif response.lower() == "open youtube" :
        os.system("say opening youtube")
        os.system("open -a safari 'https://www.youtube.com'")
    elif query[0] == "google" :
        os.system("open -a safari 'https://www.google.com/search?q='"+query[1])
        os.system("say opening google")
    # offline_speak(jarvis_speech)
