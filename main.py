import os
import threading
from flask import Flask
import telebot

# Получаем токен из настроек или используем указнный
TOKEN = os.environ.get('BOT_TOKEN', '8762393896:AAErKClh5LyG9LS9yihqicFS_taQ28zfOwc')
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# Страница для проверки работы сервера
@app.route('/')
def home():
    return "Native Studio Bot Active!", 200

# Ответ на команду /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Приветствую, я помощник Native Studio.")

def run_bot():
    print("Бот запускается...")
    bot.infinity_polling(skip_pending=True)

if __name__ == '__main__':
    # Запускаем бота в фоновом режиме
    threading.Thread(target=run_bot, daemon=True).start()
    
    # Запускаем веб-сервер для Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
