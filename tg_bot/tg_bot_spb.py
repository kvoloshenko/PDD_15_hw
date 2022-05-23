import telebot
import pprint
import time
import os
import parser_html.parser_v01 as p

# pyTelegramBotApi (основная библиотека) документация https://github.com/eternnoir/pyTelegramBotAPI
# pyTelegramBotApi (основная библиотека) proxy https://github.com/eternnoir/pyTelegramBotAPI под заголовком proxy

token = 'MY_TOKEN'

# Чтение файла
with open('token', 'r') as f:
    # 1. Прочитать сразу все данные
    token = f.read()
    # print(token)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = 'You can get news from https://saint-petersburg.ru/ \nThe following commands are available:\n/covid – News about covid in Sankt-Petersburg\n/where - Where to go in Sankt-Petersburg\n'
    bot.reply_to(message, text)


# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)


# @bot.message_handler(content_types=['text'])
# def reverse_text(message):
#     print(message)
#     text = message.text[::-1]
#     bot.reply_to(message, text)

# @bot.message_handler(content_types=['sticker'])
# def send_sticker(message):
#     print(message)
#     # FILE_ID = 'CAADAgADPQMAAsSraAsqUO_V6idDdBYE'
#     FILE_ID = 'CAACAgIAAxkBAAM3YotOZuDBf3Ou-FBpE2TrQ3WFH6MAAkEDAAK6wJUFq5JgMydOW6kkBA'
#     bot.send_sticker(message.chat.id, FILE_ID)

@bot.message_handler(commands=['covid', 'where'])
def say(message):
    print(message)
    if message.text == '/covid':
        text = 'Current Covid News:\n'
        items = p.get_news('covid')
    else:
        text = 'Where to go in Sankt-Petersburg:\n'
        items = p.get_news('where')
    for item in items:
        text += f'{item["date"]} {item["item_header"]} {item["url"]}\n'
    bot.reply_to(message, text)


bot.infinity_polling()

