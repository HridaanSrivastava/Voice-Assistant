import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import pyjokes
from PyDictionary import PyDictionary

x = sr.Recognizer()
a = pyttsx3.init()
dict = PyDictionary()

voices = a.getProperty('voices')
a.setProperty('voice', voices[1].id)

def tts(text):
    a.say(text)
    a.runAndWait()

def input():
    try:
        with sr.Microphone() as mic:
            x.adjust_for_ambient_noise(mic, duration=0.3)
            print("Listening..")
            audio = x.listen(mic)
            rec = x.recognize_google(audio)
            rec = rec.lower()
            if "python" in rec:
                rec = rec.replace("python","")
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
    return rec

def assistant():
    rec = input()
    if "play" in rec:
        song=rec.replace("play","")
        print("Playing"+song)
        tts("Playing"+song)
        pywhatkit.playonyt(song)

    elif "who is" in rec:
        person=rec.replace("who is","")
        person_info=wikipedia.summary(person,1)
        print(person_info)
        tts(person_info)

    elif "time" in rec:
        time=datetime.datetime.now().strftime("%I:%M %p")
        print("The current time is "+time)
        tts("The current time is "+time)

    elif "joke" in rec:
        joke=pyjokes.get_joke()
        print(joke)
        tts(joke)
    
    elif "what is" in rec:
        word=rec.replace("what is","")
        meaning = dict.meaning(word) 
        print(meaning)
        tts(meaning)
    
    elif "who are you" in rec:
        print("I am python, your virtual assistant")
        tts("I am python, your virtual assistant")

assistant()