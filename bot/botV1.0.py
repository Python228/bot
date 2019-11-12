import telebot



bot = telebot.TeleBot('999602825:AAFLxnk1nvT3zZY-ZCuZIeSLMoAqOVwZnh4')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard3 = telebot.types.ReplyKeyboardMarkup()
keyboard4 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока', 'Помогите')
#keyboard1.row('Hello', 'Goodbye', 'Help')
keyboard2.row('ТСД', 'Касса', '1С')
keyboard3.row('9000', 'АТОЛ', 'ШТРИХ-М', 'Назад')
keyboard4.row('подключение ТСД к ПК по USB', 'Не работает сканер на устройстве', 'UROVO не проходит тест связи', 'Назад')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text == 'Помогите':
        bot.send_message(message.chat.id, 'Какой у вас вопрос?', reply_markup=keyboard2)
    elif message.text == 'Касса':
        bot.send_message(message.chat.id, 'Выберите модель', reply_markup=keyboard3)
    elif message.text == '9000':
        bot.send_message(message.chat.id, 'https://support.rightscan.ru/knowledge-bases/4-oborudovanie-i-po/categories/307-mkassa-rs9000-f/articles')
    elif message.text == 'ТСД':
        bot.send_message(message.chat.id, 'Выберите модель', reply_markup=keyboard4)
    elif message.text == 'подключение ТСД к ПК по USB':
        bot.send_message(message.chat.id, 'https://support.rightscan.ru/knowledge-bases/4/articles/1810-urovo-kak-podsoedenit-tsd-k-pk-po-usb')
    elif message.text == 'Не работает сканер на устройстве':
        bot.send_message(message.chat.id, 'https://support.rightscan.ru/knowledge-bases/4/articles/2083-tsd-urovo-ne-rabotaet-skaner-na-ustrojstvah-tsd')
    elif message.text == 'UROVO не проходит тест связи':
        bot.send_message(message.chat.id, 'https://support.rightscan.ru/knowledge-bases/4/articles/2259-urovo-ne-prohodit-test-svyazi')
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)









@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()