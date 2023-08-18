import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import random
import os 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I'm your personal assistant. Tell me how can i help you.")

def listenCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n")
    except Exception:
        speak("Please say that again!")
        print("Please say that again!")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = listenCommand().lower()
        if 'quit' in query:
            print("Quitting sir..! Thanks for using me, have a great day")
            speak("Quitting sir..! Thanks for using me, have a great day")
            exit()
        
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")
        
        elif 'open stack overflow' in query:
            speak("Opening Stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        
        elif 'play music' in query:
            speak("Playing Music")
            album = "E:\\Python\\Python Harry\\music"
            songs = os.listdir(album)
            length = len(songs)
            randNo = random.randint(0,length)
            os.startfile(os.path.join(album,songs[randNo]))
