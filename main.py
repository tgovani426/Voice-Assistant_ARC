import ctypes
import os
import subprocess
import webbrowser

import pyaudio
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import winshell as winshell

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    time = int(datetime.datetime.now().hour)
    if 0 <= time < 21:
        speak("Good morning Sir!!")
    elif 12 <= time < 18:
        speak("Good Afternoon sir!!")
    else:
        speak("Good Evening sir!!")

    astname = "Arc 1 point 1"
    speak("I am your assistant")
    speak(astname)


def takeCommand():

    listner = sr.Recognizer()

    with sr.Microphone() as source:
        listner.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        listner.pause_threshold = 1
        audio = listner.listen(source)
    try:
        print("Recognizing...")
        cmd = listner.recognize_google(audio)
        print(f"You said :{cmd}")

    except Exception as exp:
        print(exp)
        print("Unable to Recognize your Voice.")
        return None
    return cmd


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    # wishMe()

    while True:
        command = takeCommand().lower()

        if 'open youtube' in command:
            speak("Welcome to youtube!!")
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            speak("opening Google")
            webbrowser.open("google.com")

        elif 'play' in command:
            song = command.replace("play", "")
            speak("playing"+song)
            pywhatkit.playonyt(song)

        elif 'exit' == command:
            speak("Thanks for giving your time.")
            exit()

        elif 'lock window' == command:
            speak("Locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown the system' == command:
            speak("please give my password")
            pswd = takeCommand()
            print(pswd)
            if pswd == "123":
                speak("Password accepted!!")
                speak("Your device is going in Deep sleep,Good bye")
                subprocess.call('shutdown /p /f')

        elif 'hibernate the system' in command:
            speak("Your device will enter into hibernate Mode.")
            subprocess.call("shutdown /h")

        elif 'empty recycle bin' == command:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")






