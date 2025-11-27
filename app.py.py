import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser
import os
import random

# === CONFIGURATION === #
user_name = "GOKUL"  # Change to your name

# === INITIALIZATION === #
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)


def engine_talk(text):
    print(f"Goks is saying: {text}")
    engine.say(text)
    engine.runAndWait()


def greet_user():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        greeting = f"Good morning, {user_name}!"
    elif 12 <= hour < 17:
        greeting = f"Good afternoon, {user_name}!"
    elif 17 <= hour < 22:
        greeting = f"Good evening, {user_name}!"
    else:
        greeting = f"It's late, {user_name}. Hope you're doing well!"
    engine_talk(greeting)


def user_commands():
    try:
        with sr.Microphone() as source:
            print("Start Speaking!!")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower().strip()
            print(f"User said: {command}")

            if 'goks' in command:
                command = command.replace('goks', '').strip()
            return command

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("Network error. Please check your internet connection.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return ""


def open_app(app_name):
    if 'notepad' in app_name:
        os.system("start notepad")
        engine_talk("Opening Notepad")
    elif 'chrome' in app_name:
        os.system("start chrome")
        engine_talk("Opening Google Chrome")
    elif 'calculator' in app_name:
        os.system("start calc")
        engine_talk("Opening Calculator")
    else:
        engine_talk("Application not recognized or not supported yet.")


def ai_style_response(command):
    responses = {
        "how are you": "I'm just a bunch of code, but I'm doing great!",
        "what can you do": "I can play music, tell jokes, open apps, and much more!",
        "who created you": "I was created by a brilliant developer, with some help from OpenAI tech."
    }
    for key in responses:
        if key in command:
            return responses[key]
    return "I'm still learning! Can you try asking something else?"


def run_Goks():
    command = user_commands()
    if command:

        if 'play' in command:
            song = command.replace('play', '').strip()
            engine_talk(f'Playing {song}')
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            engine_talk(f'The current time is {time}')

        elif 'date' in command:
            date = datetime.datetime.now().strftime('%A, %d %B %Y')
            engine_talk(f"Today's date is {date}")

        elif 'who is' in command:
            person = command.replace('who is', '').strip()
            try:
                info = wikipedia.summary(person, 1)
                print(info)
                engine_talk(info)
            except wikipedia.exceptions.DisambiguationError:
                engine_talk("There are multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                engine_talk("Sorry, I couldn't find any information on that.")

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            engine_talk(joke)

        elif 'fact' in command:
            try:
                topic = random.choice(['space', 'ocean', 'history', 'technology', 'human body'])
                fact = wikipedia.summary(topic, 1)
                engine_talk("Here's a random fact:")
                engine_talk(fact)
            except Exception:
                engine_talk("Couldn't fetch a fact right now.")

        elif 'search' in command:
            search_term = command.replace('search', '').strip()
            engine_talk(f'Searching {search_term} on Google')
            webbrowser.open(f"https://www.google.com/search?q={search_term}")

        elif 'open' in command:
            app_name = command.replace('open', '').strip()
            open_app(app_name)

        elif 'send message' in command:
            engine_talk("Who do you want to send a message to?")
            number = "+911234567890"  # Replace this
            message = "Hello from Goks!"
            time_hour = datetime.datetime.now().hour
            time_minute = datetime.datetime.now().minute + 1
            pywhatkit.sendwhatmsg(number, message, time_hour, time_minute)
            engine_talk("Sending your message shortly.")

        elif 'stop' in command or 'exit' in command or 'quit' in command:
            engine_talk(f"Goodbye {user_name}! Take care.")
            sys.exit()

        else:
            response = ai_style_response(command)
            engine_talk(response)

    else:
        engine_talk("I did not catch that. Please speak again.")


# Start with a greeting
greet_user()

# Run assistant continuously
while True:
    run_Goks()
