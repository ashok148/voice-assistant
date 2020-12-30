import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():       
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour>=12 and hour <18:
        speak('Good Afternoon!')
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir, Please tell me how may I help you")    

def takeCommand():        # It will take microphone input and return string output
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...') 
        query = r.recognize_google(audio, language='en-in')   
        print(f"user said: {query}\n")

    except Exception:
        speak('error...')

        print("Say that again please...")
        return "None"
    return query  

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ashokkumar56624@gmail.com'," password")
    server.sendmail('ashokkumar56624@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
      query = takeCommand().lower()

    if 'quit' in query:
        exit()  
    
    if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
 
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open geeksforgeeks' in query:
        webbrowser.open("geeksforgeeks.com")

    elif 'open gmail' in query:
        webbrowser.open("gmail.com")

    elif 'play music' in query:
        music_dir = 'E:\\ASHOK KUMAR\\AUDIO'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[3]))

    elif 'tell me the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")  
        speak(f"Sir, the time is {strTime}")


    elif 'open code' in query:
        codePath = "a\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)    

    elif 'send email to Ashok kumar' in query:
        try:
            speak("What should is send?")
            content = takeCommand()
            to = "ashokyourEmail@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent!")
        except Exception as e:
            print(e) 
            speak("Sorry, I am not able to send your email!!!")   

        
