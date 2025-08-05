import speech_recognition as sr
import time
import threading

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"⏳ Listening... {i} seconds left", end='\r')
        time.sleep(1)
    print("\n🛑 Done listening.")

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        listen_time = 30  # You can change this to any number of seconds

        # Start countdown in background
        timer_thread = threading.Thread(target=countdown, args=(listen_time,))
        timer_thread.start()

        print("🎙️ Start speaking now...")
        audio = recognizer.record(source, duration=listen_time)

        try:
            text = recognizer.recognize_google(audio)
            print("\n✅ You said:\n", text)
        except sr.UnknownValueError:
            print("\n⚠️ Could not understand your voice.")
        except sr.RequestError:
            print("\n❌ Could not connect to the speech recognition service.")

if __name__ == "__main__":
    main()
