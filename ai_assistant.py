import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use a female voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email@gmail.com', 'your-password')
    server.sendmail('your-email@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wish_me()
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            query = take_command().lower()
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia, ")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query:
            music_dir = 'path-to-your-music-directory'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = take_command()
                speak("Whom should I send it to?")
                to = take_command()
                send_email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")
        elif 'exit' in query:
            speak("Goodbye Sir!")
            exit()
        elif 'who are you' in query:
            speak("I am your AI assistant, designed to assist you with various tasks!")
        elif 'what can you do' in query:
            speak("I can perform various tasks such as searching on Wikipedia, opening websites, playing music, sending emails, and more!")
        else:
            speak("Sorry, I didn't understand that. Can you please repeat?")