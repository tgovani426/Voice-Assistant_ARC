import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass
    return command


def run_marry():
    command = take_command()
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is " + time)

    elif 'jokes' in command:
        talk(pyjokes.get_joke())

run_marry()
