import speech_recognition as sr 
import pyttsx3
import datetime
import os
import shutil

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning  !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon  !") 

	else:
		speak("Good Evening  !") 

	assname =("Tifity")
	speak("I am your Assistant")
	speak(assname)
	

def username():
	speak("What should i call you")
	uname = takeCommand()
	speak("Welcome")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	
	print("Welcome ", uname.center(columns))
	
	
	speak("How can i Help you today.")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...") 
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e) 
		print("Unable to Recognize your voice.") 
		return "None"
	
	return query

def get_time():
    now=datetime.datetime.now()
    hour=now.strftime("%I")
    minute=now.strftime("%M")
    am_pm=now.strftime("%p")
    speak(f"the time is {hour}:{minute} {am_pm}")

if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()
     
    while True:
         
        query = takeCommand().lower()
		
        if 'What is the time' in query:
            get_time()
			
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you.")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
			
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me Tifity")
            print("My friends call me Tifity")
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()