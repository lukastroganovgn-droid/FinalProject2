import os
import telebot
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TOKEN")

bot = telebot.TeleBot(api_key)
