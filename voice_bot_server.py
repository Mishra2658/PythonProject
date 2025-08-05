import asyncio
import websockets
import speech_recognition as sr
from gtts import gTTS
import os
import random

responses = [
    "Yeah, good. Tell more.",
    "Okay, now I got it.",
    "Very sad, tell more.",
    "Stop it nowww!",
    "I wanna know more."
]

def speak_text(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    os.system("start response.mp3")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=10)
            text = recognizer.recognize_google(audio)
            print("📝 You said:", text)
            return text
        except Exception as e:
            return "Sorry, I couldn't understand that."

async def handle_client(websocket):  # ✅ Removed 'path'
    print("🔗 Client connected")
    try:
        while True:
            msg = await websocket.recv()
            print(f"📥 Received: {msg}")

            if msg == "stop":
                await websocket.send("🔌 Connection stopped by client.")
                break

            elif msg in ("start", "continue"):
                user_input = recognize_speech()
                bot_reply = random.choice(responses)

                print("🤖 Bot:", bot_reply)
                speak_text(bot_reply)

                await websocket.send(f"User: {user_input}\nBot: {bot_reply}")
            else:
                await websocket.send("❗ Unknown command. Use: start, continue, or stop.")
    except Exception as e:
        print(f"💥 Server error: {e}")

async def start_server():
    print("🚀 Starting WebSocket server on ws://localhost:6789")
    async with websockets.serve(handle_client, "localhost", 6789):  # ✅ No 'path'
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(start_server())
