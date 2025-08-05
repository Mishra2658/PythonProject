import websocket

def on_message(ws, message):
    print("📥 Received from server:")
    print(message)

def on_error(ws, error):
    print("❌ Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("🔌 Connection closed")

def on_open(ws):
    print("🚀 Connected to server")
    ws.send("start")  # Trigger the server

# Create WebSocket connection
ws = websocket.WebSocketApp(
    "ws://localhost:6789",
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

# Run the client
ws.run_forever()
