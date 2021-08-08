import os
from dotenv import load_dotenv
import telebot

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'hi'])

def send_welcome(message):
    bot.reply_to(message, "Hi, how are you doing?")

@bot.message_handler(commands=['help', 'gethelp'])

def help(message):
    bot.send_message(message.chat.id, "How I can help you?")

bot.polling()