import os
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'hi'])

def send_welcome(message):
    bot.reply_to(message, "Hi, how are you doing?")

#keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('Available commands')
item2 = types.KeyboardButton('Done')
markup.add(item1, item2)
@bot.message_handler(commands=['help', 'gethelp'])

def help(message):
    bot.send_message(message.chat.id, "How I can help you?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def keyboard(message):
    if message.chat.type == 'private':
        if message.text == 'Available commands':
            bot.send_message(message.chat.id, 'start, hi, Available commands, Done')
        elif message.text == 'Done':
            bot.send_message(message.chat.id, 'Ok, got it. Have a nice day')
        else:
            bot.send_message(message.chat.id, 'Sorry, I dont understand you. Try again later')

bot.polling()

