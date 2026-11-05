import os
import telebot
from dotenv import load_dotenv
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from main import get_answer

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

def get_main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_delivery = KeyboardButton("Доставка")
    btn_payment = KeyboardButton("Оплата")
    btn_return = KeyboardButton("Возврат и гарантия")
    btn_price = KeyboardButton("Цена")
    btn_assortment = KeyboardButton("Ассортимент")
    
    markup.add(btn_delivery, btn_payment, btn_return, btn_price, btn_assortment)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, 
        "Привет! Я бот-поддержка. Выбери тему из меню ниже или напиши свой вопрос текстом.", 
        reply_markup=get_main_keyboard()
    )

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Просто напиши свой вопрос текстом или нажми кнопку из меню.", reply_markup=get_main_keyboard())

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Если пользователь нажал на кнопку, текст кнопки придет сюда же
    answer = get_answer(message.text)
    bot.reply_to(message, answer, parse_mode='Markdown', reply_markup=get_main_keyboard())

print("Бот запущен...")
bot.infinity_polling()