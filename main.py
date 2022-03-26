import ctypes
import datetime
import json
import os
import subprocess
import webbrowser
from urllib import request
from cv2 import VideoCapture, imshow, waitKey, destroyWindow, imwrite
import pyttsx3
import pywhatkit
import speech_recognition as sr
import winshell as winshell

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def Greeting():
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
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        listener.pause_threshold = 1
        audio = listener.listen(source)
    try:
        cmd = listener.recognize_google(audio)
        print("Recognizing...")
        print(f"You said :{cmd}")
        return cmd

    except Exception as exp:
        print(exp)
        print("Unable to Recognize your Voice.")
        return None


def git_search(user_name):
    response = request.urlopen("https://api.github.com/users/" + user_name)
    data = json.loads(response.read())

    github_url = data["html_url"]
    name = str(data["name"])
    repo = str(data["public_repos"])
    num_follower = str(data["followers"])
    num_following = str(data["following"])
    bio = str(data["bio"])

    github_resource = [name, num_follower, num_following, repo, bio, github_url]
    return github_resource


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    Greeting()

    while True:
        command = takeCommand().lower()

        if 'open youtube' == command:
            speak("Welcome to youtube!!")
            webbrowser.open("youtube.com")

        elif 'open google' == command:
            speak("opening Google")
            webbrowser.open("google.com")

        elif 'play' in command:
            song = command.replace("play", "")
            speak("playing" + song)
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

        elif "where is" in command:
            command = command.replace("where is", "")
            location = command
            speak(f"You ask me to locate {location}")
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif "github" in command:
            speak("welcome to GitHub!!")
            speak("Kindly enter the user name")
            user = input("PLEASE ENTER THE USER NAME:\t")
            result = git_search(user)
            speak(f"{result[0]} is a developer with {result[1]} followers and {result[2]} repository  ")
            speak(f"Do you want to open account of {result[0]} ??")
            ans = takeCommand()
            if ans == "yes":
                speak(f"Bio of {result[0]}")
                webbrowser.open(url=f"{result[5]}")

        elif "news" in command:
            try:
                jsonObj = request.urlopen(
                    '''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=383da4193fd2451599997e4f6902cad5''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    speak(item["description"])
                    i += 1
            except Exception as e:

                print(str(e))

        elif "camera" in command or "take photo" in command:
            cam_port = 0
            cam = VideoCapture(cam_port)

            result, image = cam.read()
            date = datetime.datetime.now().strftime("%I%M%S")
            if result:
                filename = "file_%s.png"%date
                directory = "\\Users\\Tirth\\PycharmProjects\\Arc\\Images"
                os.chdir(directory)

                imshow(filename, image)
                imwrite(filename, image)
                waitKey(0)
                destroyWindow(filename)
            else:
                print("No image detected. Please! try again")

