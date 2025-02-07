import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Load environment variables
TELEGRAM_BOT_TOKEN = os.getenv("7999116953:AAHSUmkWs0aDrXNmYIbhJlC5O4VL8gl4ky4")
CHAT_ID = os.getenv("7378447394")

# Ensure both variables exist
if not TELEGRAM_BOT_TOKEN or not CHAT_ID:
    raise ValueError("Missing TELEGRAM_BOT_TOKEN or CHAT_ID in environment variables.")

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

@app.route("/")
def home():
    return "Telegram News Bot is running!"

@app.route("/save", methods=["POST"])
def save_news():
    data = request.get_json()
    if not data or "title" not in data or "url" not in data:
        return jsonify({"error": "Invalid request"}), 400

    title = data["title"]
    url = data["url"]

    # Send message to Telegram
    message = f"📰 *{title}*\n🔗 [Read More]({url})"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}

    response = requests.post(TELEGRAM_API_URL, json=payload)

    if response.ok:
        return jsonify({"success": True, "message": "News sent to Telegram!"})
    else:
        return jsonify({"error": "Failed to send message"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
