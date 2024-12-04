
import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import os
import musicLibrary
import pyjokes

recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
  hour = datetime.datetime.now().hour
  if hour <= 12:
    speak("Good Morning Sir")
  elif 12 <= hour < 18:
    speak("Good Afternoon Sir")
  else:
    speak("Good Evening Sir")
  speak("Jarvis at your service. How can I help you?")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
            return "None"
        except sr.RequestError:
            speak("Network error. Please check your connection.")
            return "None"

def speak_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}.")


def get_joke():
    joke = pyjokes.get_joke()
    speak(joke)


def execute_command(command):
    """Executes tasks based on the user's command."""
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}.")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "open instagram" in command:
       webbrowser.open("https://www.instagram.com")
       speak("Opening Instagram.")
    elif "open facebook" in command:
       webbrowser.open("https://www.facebook.com")
       speak("Opening Facebook.")
    elif "play music" in command:
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        speak("Playing music.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("I'm sorry, I can't help with that yet.")


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Present")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
    greet()
    while True:
        user_command = listen()
        if user_command != "None":
            execute_command(user_command)