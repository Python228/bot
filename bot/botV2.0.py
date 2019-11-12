from mailbox import Message

import telebot
import random

#TOKEN = '999602825:AAFLxnk1nvT3zZY-ZCuZIeSLMoAqOVwZnh4'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message,'Какой вопрос?')

@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
#    bot.reply_to(message, str(random.random()))
    if 'Ted' in message.text:
        bot.reply_to(message, 'Hi Ted')
        return

@bot.edited_message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    print(message)
    print(message.sticker)


bot.polling(timeout=60)