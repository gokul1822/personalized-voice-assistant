🧠 GOKS.AI – Your Personal Mini Voice Assistant

GOKS.AI is a Python-based mini voice assistant capable of interacting with users through natural voice commands. It performs tasks like playing music, telling time and date, searching Wikipedia, opening apps, telling jokes, and simulating intelligent responses — making human–computer interaction smooth and intuitive.


GOKS_AI_Documentation(mini proj…

📌 Features

🎤 Voice Recognition (Speech-to-text using Google API)

🔊 Text-to-Speech Responses using pyttsx3

🎵 Play Music on YouTube via pywhatkit

📅 Tell Date & Time

📚 Wikipedia Search & Summaries

😂 Tells Jokes using pyjokes

💻 Open System Applications

🌐 Web Search & Automation

🤖 Basic AI-like Conversational Ability

🛠 Technologies Used

Python 3.x

Google Speech Recognition API

pyttsx3 (Text-to-Speech)

Wikipedia API

PyWhatKit (YouTube Automation)

PyJokes

OS Module

Datetime Module

Webbrowser

📦 Required Python Libraries
speechrecognition
pyttsx3
pywhatkit
wikipedia
pyjokes
pyaudio
os
datetime
webbrowser
sys
random


Install them using:

pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes pyaudio

⚙️ How GOKS.AI Works (Workflow)

🎙 User speaks a command

🧠 Speech recognized using Google API

🔍 Command analyzed to detect action (play, time, who is, tell joke...)

⚡ Action executed using corresponding libraries

🔊 Response spoken back using Text-to-Speech engine


GOKS_AI_Documentation(mini proj…

💻 Basic Code Example
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

engine.say("Hello, I am GOKS.AI. How can I help you?")
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(f"You said: {command}")
except:
    print("Sorry, I didn't get that.")


GOKS_AI_Documentation(mini proj…

🧪 Sample Output

Terminal Output:

Listening...
You said: play despacito


Voice Output:
➡️ “Playing Despacito”

✅ Results

GOKS.AI successfully performs:

✔ Voice recognition

✔ Time & date response

✔ Music playback

✔ Wikipedia information

✔ Jokes

✔ Application opening

✔ Conversational responses


GOKS_AI_Documentation(mini proj…

📁 Project Structure (Suggested)
GOKS-AI/
│── main.py
│── README.md
│── requirements.txt
│── assets/ (optional)
│── modules/ (optional)

🚀 How to Run

Install dependencies

Connect a microphone

Run:

python main.py

👨‍💻 Author

A. Gokulkrishnan
B.Tech Artificial Intelligence & Data Science
Aspiring Software Engineer
