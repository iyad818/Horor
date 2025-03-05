from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return 'Koyeb Bot is running!'

@app.route('/start-bot')
def start_bot():
    try:
        # تشغيل ملف bot.py باستخدام subprocess
        subprocess.Popen(['python3', 'bot.py'])
        return 'Bot has started successfully!'
    except Exception as e:
        return f'Failed to start the bot: {str(e)}'

if __name__ == "__main__":
    # التأكد من تشغيل التطبيق على المنفذ المناسب
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
