import os
import telebot

from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))


def send_message(data):
    consumer = 534017474
    bot.send_message(consumer, data)
