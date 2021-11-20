# import clipboard
import datetime
# import os
# import psutil
import pyautogui
# import pyjokes
import pyttsx3
import pywhatkit
import requests
# import smtplib
import speech_recognition as sr
# import time as ti
import webbrowser as we
# from email.message import EmailMessage
from newsapi import NewsApiClient
from setup import *

from time import sleep

user = "Andy"
assistant= "Gigabit" # Iron man Fan

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 1)  # Volume 0-1
engine.setProperty('voice',voices[1].id)

def output(audio):
    # print(audio) # For printing out the output
    engine.say(audio)
    engine.runAndWait()

def greet():
    # print(datetime.datetime.now().strftime("%I:%M"))
    hour = datetime.datetime.now().hour
    if (hour >= 6) and (hour < 12):
        output(f"Good Morning {user}, {assistant} here to help")
    elif (hour >= 12) and (hour < 18):
        output(f"Good afternoon {user}, {assistant} here to help")
    elif (hour >= 18) and (hour < 21):
        output(f"Good Evening {user}, {assistant} here to help")

def weather():
    output(f"In Cluj Napoca")
    city = "Cluj-Napoca"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    output(
        f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")

def inputCommand():
    # query = input() # For getting input from CLI
    r = sr.Recognizer()
    query = ""
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            query = r.recognize_google(r.listen(source), language="en_US")
        except Exception as e:
            output("Say that again Please...")
    return query

def news():
    newsapi = NewsApiClient(api_key='05fbef0165ce4124aac6080dd1e3ee27')
    output("What topic you need the news about")
    topic = inputCommand()
    data = newsapi.get_top_headlines(
        q=topic, language="en", page_size=5)
    newsData = data["articles"]
    for y in newsData:
        output(y["description"])

def sendWhatMsg():
    user_name = {
        'Jarvis': '+40786575037'
    }
    h = datetime.datetime.now().strftime('%H')
    m = datetime.datetime.now().strftime('%M')
    try:
        pywhatkit.sendwhatmsg('+40743868785', 'Me sugi.',int(h),int(m)+1)
    except Exception as e:
        print(e)
        output("Unable to send the Message")

greet()

while True:

    query = inputCommand().lower()

    if ('weather' in query):
        weather()

    elif('hello' in query):
        greet()
    
    elif('news' in query):
        news()

    if ("time" in query):
        output("Current time is " +
               datetime.datetime.now().strftime("%I:%M"))

    elif ('date' in query):
        output("Current date is " + str(datetime.datetime.now().day)
               + " " + str(datetime.datetime.now().month)
               + " " + str(datetime.datetime.now().year))

    elif('fuck you'in query):
        output("Fuck your mama")

    elif('whatsapp' in query):
        sendWhatMsg()