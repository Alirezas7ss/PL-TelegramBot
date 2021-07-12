import os
import telebot
from api import doge
from image import coin
import time

TOKEN = os.environ['API_TOKEN']


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
  bot.reply_to(msg,'''
  سلام من بات دوج کوینم و هر وقت که بهم بگید بهتون قیمت لحظه ی دوج کوین رو میدم
  ''')

@bot.message_handler(commands=['doge', 'Doge', 'DOGE'])
def doge_coin(msg):
  coin(doge())

  time.sleep(1)
  photo = open('image.jpg', 'rb')
  bot.send_photo(msg.chat.id, photo)


bot.polling()
