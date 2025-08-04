import pyttsx3

engine = pyttsx3.init()
users = ["Harsh", "Deepak", "Anjali"]
name = input("Enter your name: ")
if name in users:
    engine.say(f"Welcome {name}, you are logged in.")
else:
    engine.say("Access Denied.")
engine.runAndWait()
