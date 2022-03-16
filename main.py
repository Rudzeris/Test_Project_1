import telebot
import datetime
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    username = message.from_user.username
    msg=''
    f = open(f'log {username}.txt', 'a')

    if message.text == 'Привет':
        msg = f'Привет {username}! Хочешь анекдот?'
        bot.send_message(message.from_user.id, msg)
    elif message.text == 'Нет' or message.text == 'нет':
        msg = f'Ну, давай. Хотя бы улыбнешься.\tСогласен?'
        bot.send_message(message.from_user.id, msg)
    elif message.text == 'Да' or message.text == 'да':
        msg = f'Анекдота нет! Повёлся.'
        bot.send_message(message.from_user.id, msg)
    elif message.text == 'хочу' or message.text == 'Хочу':
        msg = f'Нужно писать "Да" или "Нет"'
        bot.send_message(message.from_user.id, msg)
    else:
        msg = f'Я тебя не понимаю =('
        bot.send_message(message.from_user.id, msg)

    # Записываем логи в файл с id пользователем
    f.write(f'{datetime.datetime.now()}:\t{message.text}\n')
    if msg!='':
        f.write(f'{datetime.datetime.now()}:\t{msg}\n')
    f.close()

bot.polling()
