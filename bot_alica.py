import random

import telebot

API_TOKEN = '6176023909:AAG24Od7XFpoLPCxfSrR0Ht7DoSy79lzJTE'

bot = telebot.TeleBot(API_TOKEN)
from telebot import types

films = [" 1+1 (Неприкасаемые)", "Миссия невыполнима", "Достучаться до небес", "Карты, деньги, два ствола!",
         "Гарри Поттер и узник Азкабана", "Один дома", "Маска",
         "Большой куш", "День сурка", "Евротур",
         "Форсаж", " Адреналин", "Дом Франкенштейна", "Без лица", "Доктор Хаус", "Побег из Нью‑Йорка", "Ронин",
         "Люди в чёрном",
         "Игра престолов", "Дневники вампира", "Сверхъестественное", "Теория большого взрыва", "Друзья",
         "Остаться в живых",
         "Как я встретил вашу маму", "Властелин колец 3: Возвращение Короля ", "Зеленая миля ",
         "Пираты Карибского моря: Проклятие Черной жемчужины ", "Судья Дредд 3D", "Фантазм 2",
         "Звездные войны: Эпизод 5 - Империя наносит ответный удар", "Престиж"
         ]
keyboard = types.InlineKeyboardMarkup()
key_films = types.InlineKeyboardButton(text='Фильм', callback_data='films')
keyboard.add(key_films)

# @bot.message_handler()
# def send_welcome(message):
#     bot.reply_to(message,message.text)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я послан служить тебе")
        bot.send_message(message.from_user.id, text='Выбери свой фильм', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "films":
        msg = random.choice(films)
        bot.send_message(call.message.chat.id, msg)




if __name__ == "__main__":
    bot.infinity_polling()
