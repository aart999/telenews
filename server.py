from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 🔹 Replace with your actual Telegram bot token
TELEGRAM_BOT_TOKEN = "7999116953:AAHSUmkWs0aDrXNmYIbhJlC5O4VL8gl4ky4"

# 🔹 Replace with your actual Telegram chat ID (user or group)
CHAT_ID = "7378447394"

@app.route('/save', methods=['POST'])
def save_news():
    data = request.json
    title = data.get("title")
    url = data.get("url")

    # Check if both title and URL are provided
    if not title or not url:
        return jsonify({"error": "Missing title or URL"}), 400

    # Format the message
    message = f"📰 *{title}*\n[Read More]({url})"

    # Telegram API URL
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    # Payload to send message to Telegram
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    # Send the request to Telegram
    response = requests.post(telegram_url, json=payload)

    # Return Telegram API response
    return response.json()

if __name__ == "__main__":
    app.run(port=5000, debug=True)

@app.route('/')
def home():
    return "API is running!", 200
