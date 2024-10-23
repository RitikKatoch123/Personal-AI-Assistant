import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyautogui
import time
import wikipedia
import webbrowser
import pyjokes
import psutil
import winshell
from cam import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..............")
        r.adjust_for_ambient_noise(source, duration=0.5)
        r.pause_threshold = 0.8
        audio = None
        while audio is None:  # Keep listening until we get valid audio
            try:
                audio = r.listen(source, timeout=4, phrase_time_limit=7)
                print("Recognizing.........")
                query = r.recognize_google(audio, language="en-in")
                print(f"User said: {query}\n")
                return query
            except sr.WaitTimeoutError:
                print("Timeout, listening again...")
            except sr.UnknownValueError:
                speak("Unable to recognize your voice, please say that again.")
                return "None"

def username():
    speak("What should I call you, sir?")
    uname = takecommand()
    if uname != "None":
        speak("Welcome Mister " + uname)
        speak("How can I help you, Sir?")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am your virtual assistant Jarvis.")

def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at' + " " + usage)
    battery=str(psutil.sensors_battery())
    speak("CPU is at" + battery)



def open_spotify():
    os.system("start spotify:")  # Thi s opens the Spotify app

def play_song_on_spotify(song_name):
    open_spotify()
    time.sleep(2)  # Wait for Spotify to open
    pyautogui.hotkey('ctrl', 'l')  # Focus on the search bar
    time.sleep(0.5)
    pyautogui.typewrite(song_name)  # Type the song name
    time.sleep(1)
    pyautogui.press('enter')  # Search for the song
    time.sleep(2)
    pyautogui.press('enter')  # Play the song

def stop_spotify():
    pyautogui.hotkey('space')  # Pause the current song

if __name__ == '__main__':
    wishMe()
    username()
    while True:
        order = takecommand().lower()

        if 'how are you' in order:
            speak("I am fine, thank you.")
            speak("How are you, Sir?")

        elif 'fine' in order or 'good' in order:
            speak("It's good to know you are fine.")

        elif 'who i am' in order:
            speak("If you can talk then surely you are a human.")

        elif 'love' in order:
            speak("It is the 7th sense that destroys all other senses.")

        elif 'who are you' in order:
            speak("I am your virtual assistant Jarvis.")

        elif 'i love you' in order:
            speak("Oh my God, thank you!")

        elif 'open notepad' in order:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif 'open command prompt' in order:
            os.system("start cmd")

        elif 'open google' in order:
            speak("What should I search for?")
            search_query = takecommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'open youtube' in order:
            speak("What should I search for on YouTube?")
            search_query = takecommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

        elif 'play music' in order:
            music_dir = "C:\\Users\\YourUsername\\Music"  # Replace with your music directory
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))  # Play the first song in the directory

        elif 'the time' in order:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open calculator' in order:
            os.system("calc")

        elif 'shut down' in order:
            speak("Shutting down the system.")
            os.system("shutdown /s /t 1")

        elif 'restart' in order:
            speak("Restarting the system.")
            os.system("shutdown /r /t 1")

        elif 'log off' in order:
            speak("Logging off the system.")
            os.system("shutdown /l")

        elif 'close notepad' in order:
            os.system("taskkill /f /im notepad.exe")

        elif 'thank you' in order:
            speak("You're welcome, Sir!")

        elif 'exit' in order or 'goodbye' in order:
            speak("Goodbye, Sir. Have a nice day!")
            break

        elif 'play song on spotify' in order:
            speak("Which song would you like to play?")
            song_name = takecommand().lower()
            play_song_on_spotify(song_name)

        elif 'stop spotify' in order:
            stop_spotify()

        elif 'wikipedia' in order:
            speak("Searching...")
            order=order.replace("wikipedia","")
            results=wikipedia.summary(order,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'where is' in order:
            order=order.replace("where is","")
            location=order
            speak("Locating.....")
            speak("Location")
            webbrowser.open("https://www.google.co.in/maps/place/"+location+"")

        elif "write a note" in order:
            speak("What should i write,  sir?")
            note=takecommand()
            file=open('jarvis.txt','w')
            speak("Sir, should I include date and time as well?")
            sn=takecommand()
            if 'yes' in sn or 'sure' in sn or 'yeah' in sn:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(note)
                speak("Done Sir")
            else:
                file.write(note)
                speak("Done Sir")

        elif 'show note' in order:
            speak("Speaking notes")
            file=open('jarvis.txt','r')
            print(file.read())
            speak(file.read(6))

        elif 'joke' in order:
            speak(pyjokes.get_joke(language="en",category="neutral"))

        elif 'time' in order:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Well the time is {strTime}")

        elif 'switch window' in order:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'take a screenshot' in order or 'screenshot this' in order:
            speak('Sir,please tell me the name for this file.')
            name=takecommand().lower()
            speak('Please hold the screen')
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot captured Sir")

        elif 'cpu status' in order:
            cpu()

        elif 'empty recycle bin' in order:
            winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=True)


        elif 'camera' in order:
            cam()
