import os
from dotenv import load_dotenv
import telebot
from telebot import types
import random

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'hi'])

def send_welcome(message):
    bot.reply_to(message, "Hi, how are you doing?")

#keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('Available commands')
item2 = types.KeyboardButton('Exit')
markup.add(item1, item2)
@bot.message_handler(commands=['help', 'gethelp'])

def help(message):
    bot.send_message(message.chat.id, "How I can help you?", reply_markup=markup)

bot.polling()

