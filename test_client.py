import websocket
import time

def on_message(ws, message):
    print("📥 Server says:\n", message)
    # Example logic: if not stopped, continue after a pause
    if "Bot" in message:
        time.sleep(2)
        ws.send("continue")

def on_error(ws, error):
    print("❌ Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("🔌 Connection closed")

def on_open(ws):
    print("✅ Connected. Sending 'start'")
    ws.send("start")

ws = websocket.WebSocketApp(
    "ws://localhost:6789",
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

ws.run_forever()
