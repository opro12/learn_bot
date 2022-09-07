#импорт логирования
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

#включаем логирование
logging.basicConfig(filename='bot.log', format='[%(asctime)s] [%(levelname)s] => %(message)s', level=logging.INFO) #debag, INFO, warning, error

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')
    print(update)

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True) 

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()