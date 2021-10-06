import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib


print("initializng jarvis")
SIR = "jaeyaesh"
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("good morning" + SIR)
    elif hour>=12 and hour<18:
        speak("good afternooon" + SIR)
    else:
        speak("good evening" + SIR)
    speak("hello jaeyaesh......this is jarvis .......your personal assistant..internet speed is 1000..gb per second")
wishme()
speak("all satellites are online sir.....all systems are online.....nuclear missile is ready to launch....fixing mark 75..")

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)
time()

def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
date()

# This function will take command from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")        
        
    except Exception as e:
        print(e)
        speak("say it again please...")
        query= None
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls
    server.login('jayeshgowda30@gmail.com', 'python rsf.py')
    server.sendmail("anita.yg77@gmail.com", to, content)
    server.close()
query = takeCommand()

if 'wikipedia' in query.lower():
    speak('searching wikipedia')
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences =2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")
    
elif 'play music' in query.lower():
    songs_dir = "C:\\ncs"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[2]))

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{SIR} the time is {strTime}")
    
elif 'open code' in query.lower():
    codepath = "C:\\Users\\anita\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codepath)

elif'email to anita' in query.lower():
    try:
        speak("what should i send")
        content = takeCommand()
        to = "anita.yg77@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent successfully")

    except Exception as e:
        print(e)
