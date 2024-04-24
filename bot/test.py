import telebot
from telebot import types
from openpyxl import load_workbook
import pendulum
import sqlite3
from PIL import Image, ImageDraw, ImageFont
import io
import os

API_TOKEN = '6108466885:AAGXFfFy9Wbz8_T72M3g8QAuqCH_bZOIBB4'
bot = telebot.TeleBot(API_TOKEN)

subject_abbreviations = {
    # ... your subject abbreviations
}

# Cache for loaded schedules
loaded_schedules = {}

# Cache for generated schedule images
image_cache = {}

def init_db():
    # ... (remains the same)

def load_schedule_data(user_group):
    # ... (remains the same)

def get_schedule_from_sheet(user_group, language, day=None):
    # ... (remains the same)

def create_schedule_image(schedule, title, language):
    # ... (remains the same)

def send_schedule(chat_id, user_group, language, day=None, use_cache=True):
    # ... (remains the same)

def register_user(user_id, user_group, language, first_name=None, last_name=None, username=None):
    # ... (remains the same)

def get_user_group_and_language(user_id):
    # ... (remains the same)

# Bot command handlers

@bot.message_handler(commands=['start', 'register'])
def send_welcome(message):
    # ... (remains the same)

@bot.message_handler(commands=['reregister'])
def re_register(message):
    # ... (remains the same)

@bot.message_handler(commands=['deleteaccount'])
def delete_account(message):
    # ... (remains the same)

@bot.message_handler(commands=['help'])
def send_help(message):
    # ... (remains the same)

@bot.message_handler(commands=['admins'])
def send_admin_contact(message):
    # ... (remains the same)

@bot.message_handler(commands=['schedule'])
def send_weekly_schedule(message):
    # ... (remains the same)

@bot.message_handler(commands=['scheduletoday']) 
def send_today_schedule(message):
    # ... (remains the same)

@bot.message_handler(commands=['day']) 
def send_day_schedule(message):
    user_group, language = get_user_group_and_language(message.from_user.id)
    if not user_group:
        bot.reply_to(message, "Вы не зарегистрированы")
        return

    try:
        day = message.text.split(maxsplit=1)[1]  # Get the day from the command
    except IndexError:
        bot.reply_to(message, "Пожалуйста, укажите день недели. Например: /day Понедельник")
        return

    if not send_schedule(message.chat.id, user_group, language, day):
        bot.send_message(message.chat.id, f"Не удалось получить расписание на {day}")

@bot.message_handler(commands=['update'])
def admin_update(message):
    # TODO: Add logic for admin to update the schedule spreadsheet
    bot.reply_to(message, "Функционал обновления расписания пока в разработке.")

@bot.message_handler(commands=['notify'])
def admin_notify(message):
    # TODO: Add logic for admin to send notifications to registered users
    bot.reply_to(message, "Функционал уведомлений пока в разработке.")

if __name__ == '__main__':
    bot.polling(none_stop=True)
