import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes

print("jarvis at your service sir!!")
SIR = "jaeyaesh"
sir = "boss"
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
    speak("hello jaeyaesh....this is jarvis .......your personal assistant..internet speed is 1000..gb per second")
wishme()

speak("all satellites are online sir.....all systems are online.....nuclear missile is ready to launch....fixing mark 75..")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
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
        query = None    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls
    server.login('jayeshgowda30@gmail.com', 'python rsf.py')
    server.sendmail("anita.yg77@gmail.com", to, content)
    server.close()
query = takeCommand()


while True:
    query = takeCommand()

    if 'wikipedia' in query.lower():
        speak('searching wikipedia')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences =2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        speak(f"as you wish {sir}")
        webbrowser.open("youtube.com")

    elif 'my introduction' in query.lower():
        speak("my boss is jaeyaesh gowda.....age is 18...pure iluminati....son of lucifer")

    elif "what's the plan tonight" in query.lower():
        speak("ummm boss...playing games...some evil works")

    elif'motivate me' in query.lower():
        speak("here you go sir..... i have a line to motivate you......respect your haters..because they are the only one.. who think that you are better. than them")

    elif'call my girlfriend' in query.lower():
        speak("which one boss")

    elif'buy jarvis' in query.lower():
        speak("bye sir..have a great night with your girlfriends....hehehe")

    elif'open instagram' in query.lower():
        webbrowser.open("www.instgram.com")

    elif'identify this music' in query.lower():
        webbrowser.open("www.aha-music.com/identify-songs-music-recognition-online#record-div")

    elif 'open github' in query.lower():
        webbrowser.open("github.com")     
    
    elif 'play music' in query.lower():
        speak(f"yeah...time to concentrate boss")
        songs_dir = "C:\\Users\\anita\\Desktop\\New folder"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{SIR} the time is {strTime}")
    
    elif 'open my code' in query.lower():
        codepath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
        speak(f" opening your code {SIR}")
        os.startfile(codepath)

    elif 'open Android studio' in query.lower():
        Androidstudiopath = "C:\\Users\\anita\\Desktop\\lucifer\\lucifer.exe"
        os.startfile(Androidstudiopath)

    elif 'open facebook' in query.lower():
        webbrowser.open("www.Facebook.com")
      
    elif 'open google chrome' in query.lower():
        chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        speak(f"as you wish {SIR}")
        os.startfile(chromepath)

    elif 'open my gaming setup' in query.lower():
        BlueStacks5path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\BlueStacks5.exe"
        speak(f"ohh yeah {sir}...time for gaming")
        os.startfile(BlueStacks5path)

    elif 'tell me a joke' in query.lower():
        speak(pyjokes.get_joke())


    elif'email to anita' in query.lower():
        try:
            speak("what should i send")
            content = takeCommand()
            to = "anita.yg77@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent successfully")

        except Exception as e:
                print(e)


