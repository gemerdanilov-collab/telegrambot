import os
import threading
from flask import Flask
import telebot

# Токен берется из настроек Render
TOKEN = os.environ.get('8762393896:AAErKClh5LyG9LS9yihqicFS_taQ28zfOwc')
bot = telebot.TeleBot(8762393896:AAErKClh5LyG9LS9yihqicFS_taQ28zfOwc)

app = Flask(__name__)

# Веб-страница для проверки работы
@app.route('/')
def home():
    return "Native Studio Bot Active", 200

# Стартовая команда
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Приветствую, я помощник Native Studio.")

def run_bot():
    bot.infinity_polling(skip_pending=True)

if __name__ == '__main__':
    # Запускаем бота в фоновом потоке
    threading.Thread(target=run_bot, daemon=True).start()
    
    # Запускаем веб-сервер Flask
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
