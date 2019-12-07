import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate',150)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <12:
        speak('Good Morning Boss')
    elif 12 <= hour <18:
        speak('Good Afternoon Boss')
    else:
        speak('Good Evening Boss')
    speak('I am the Bot 1.0.. What do you want me to do?')

def takeCommand():
    #take inputs from user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said : {query}\n")
        except:
            print("Sorry Say that again please")
            return "NONE"
    return query

if __name__ == "__main__":
    #wish()
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            try:
                #enter the directory here
                music_dir = r""
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))
            except:
                print("Not able to find file")

        elif ('what\'s the time' in query) or ('the time' in query):
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"Sir,The time is {strtime}")

        elif ('open visual studio' in query) or ('open code' in query) or ('open vs code' in query):
            #add the path of vs code here
            codepath = r""
            os.startfile(codepath)

        elif 'open chrome' in query:
            #add the path of chrome here
            cpath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(cpath)

