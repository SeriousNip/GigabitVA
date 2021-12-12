import webbrowser
# import clipboard
import datetime
import time
# import os
import pyglet
# import psutil
# import pyautogui
# import pyjokes
# import playsound
import pyttsx3
import pywhatkit
import requests
# import smtplib
import speech_recognition as sr
# import time as ti
# from email.message import EmailMessage
from newsapi import NewsApiClient

assistant= "Natasha"
location=''
# def setUser(username):
#     user=username

contacts = ['+40755655535','+40743868785']

engine = pyttsx3.init('sapi5')  # TTS driver for windows operating systems
voices = engine.getProperty('voices') # voice modules built into windows
engine.setProperty('rate', 150)    # Speed in percentage (can go over 100) 100 is standard
engine.setProperty('volume', 1)  # Volume 0-1
engine.setProperty('voice',voices[1].id)    # Selecting the voice module desired from the ones installed

def output(audio):
    # print(audio) # For printing out the output
    engine.say(audio) # calling the function that makes the assistant talk
    engine.runAndWait() # Blocks while processing all currently queued commands

def greet(username):
    # print(datetime.datetime.now().strftime("%I:%M"))
    hour = datetime.datetime.now().hour
    if (hour >= 6) and (hour < 12):
        output(f"Good Morning {username}, {assistant} here to help")
    elif (hour >= 12) and (hour < 18):
        output(f"Good afternoon {username}, {assistant} here to help")
    elif (hour >= 18) and (hour < 21):
        output(f"Good Evening {username}, {assistant} here to help")

def weather(location):
    output(f"In {location}") # Output saying the location for which the weather is called
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    # Sending the request for data
    temp1 = res["weather"][0]["description"] # Extracting data from the JSON response
    temp2 = res["main"]["temp"] # Extracting data from the JSON response
    output(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}") # Outputing the actual information regarding weather

def inputCommand():
    # query = input() # For getting input from CLI
    r = sr.Recognizer() # Initializing the Speech Recognition engine
    query = "" # Initializing the variable in which we will save the recognized text
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1 # sets the threshold for pause between words
        try:
            query = r.recognize_google(r.listen(source), language="en_GB") # call for Speech Recognition using the Google Speech Recognition API
        except Exception as e:
            output("Say that again Please...") # in case of an error in the Speech Recognition it will output an error
    return query

def news():
    newsapi = NewsApiClient(api_key='05fbef0165ce4124aac6080dd1e3ee27') # Initating the News Engine
    output("What topic you need the news about")
    topic = inputCommand() # Getting the topic for the news
    data = newsapi.get_top_headlines(q=topic, language="en", page_size=5) #Getting the most important headlines on that topic
    newsData = data["articles"] # Saving the articles themselves in an auxiliary variable
    for y in newsData:
        output(y["description"]) # Outputting the news themselves

def sendWhatMsg():
    try:
        message=inputCommand() # getting the message text
        h = datetime.datetime.now().strftime('%H') # getting current hour
        m = datetime.datetime.now().strftime('%M') # getting current minute
        # the minute is in string format so it is modified to be able to send the message now 
        # (1 minute after the command was sent)        
        if(int(m)+1>59): 
            m=0
        else:
            m=int(m)+1
        pywhatkit.sendwhatmsg('+40743868785', message,int(h),m,15,True, 5) # sending the message through whastapp web
    except Exception as e:
        output("Unable to send the Message") # In case of an error the assitant says it failed to complete the request



def awaken(location):
    
    timeout = 10    # Setting timeout after which the assitant will go to sleep (in seconds)
    start_time=time.time() # Getting current time for the timeout
    while True:
        
            
        query = inputCommand().lower() # Getting the user request 

        if ('weather' in query): # Checking for the request
            weather(location)   # Calling the function for the user request
            start_time=time.time() # Reseting the time for the timeout
            

        elif('hello' in query):
            greet()
            start_time=time.time()
            
        
        elif('news' in query):
            news()
            start_time=time.time()
            

        if ("time" in query):
            output("Current time is " +
                   datetime.datetime.now().strftime("%I:%M"))
            start_time=time.time()
            

        elif ('date' in query):
            output("Current date is " + str(datetime.datetime.now().day)
                   + " " + str(datetime.datetime.now().month)
                   + " " + str(datetime.datetime.now().year))
            start_time=time.time()
            

        elif('whatsapp' in query):
            sendWhatMsg()
            start_time=time.time()
            

        elif('call the russian president' in query):
            music = pyglet.resource.media('sound.mp3')
            music.play()
            start_time=time.time()

        elif('yes' in query):
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=2VZBeeFYktQ&ab_channel=Razorshady1711")
            start_time=time.time()
             

        elif(time.time()>start_time+timeout): # Checking the timeout condition
            output("I'm going to sleep now.") # Outputing a warning that the timeout condition is being achieved
            break                             # Breaking the loop for user privacy

# awaken("Cluj")