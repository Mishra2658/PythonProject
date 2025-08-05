import asyncio
import websockets
import speech_recognition as sr
from gtts import gTTS
import os
import random

# Response pool
responses = [
    "Yeah, good. Tell more.",
    "Okay, now I got it.",
    "Very sad, tell more.",
    "Stop it nowww!",
    "I wanna know more."
]

# Convert text to speech and play
def speak_text(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    os.system("start response.mp3")  # For Windows. Use 'afplay' on Mac or 'mpg123' on Linux.

# Recognize from mic
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=10)
    try:
        text = r.recognize_google(audio)
        print("📝 You said:", text)
        return text
    except Exception as e:
        return "Sorry, I couldn't understand that."

# WebSocket handler
async def handle_client(websocket, path):
    while True:
        msg = await websocket.recv()
        if msg == "start":
            print("🔁 Triggered by Flutter: start")
            
            # 1. Convert speech to text
            user_input = recognize_speech()

            # 2. Pick random response
            bot_reply = random.choice(responses)
            print("🤖 Bot says:", bot_reply)

            # 3. Convert to speech
            speak_text(bot_reply)

            # 4. Send both texts back to Flutter
            await websocket.send(f"User: {user_input}\nBot: {bot_reply}")

# Start WebSocket server
start_server = websockets.serve(handle_client, "localhost", 6789)

print("🚀 WebSocket server running on ws://localhost:6789")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
