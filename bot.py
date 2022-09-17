"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
#импорт логирования
from asyncio.log import logger
from datetime import datetime
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import settings

#включаем логирование
logging.basicConfig( 
  format='[%(asctime)s] [%(levelname)s] => %(message)s', 
  level=logging.INFO
) 
logger = logging.getLogger(__name__)

def greet_user(update, context):
    logger.info('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')
    logger.info(update)
    

def talk_to_me(update, context):
    text = update.message.text
    logger.info(text)
    update.message.reply_text(text)

def name_planet(update, context):
    text: str = update.message.text
    entry_planet = text.split()
    planet_name = entry_planet[1]
  
    if planet_name == 'Mars':
        planet = ephem.Mars
    elif planet_name.lower() in ('Pluto', 'Плутон'):
        planet = ephem.Pluto
    else:
        update.message.reply_text('Я незнаю такой планеты((')
        return

    now = datetime.now()       
    planet_now = ephem.constellation(planet(now))

    update.message.reply_text(f'Planet: {planet_name}, {planet_now}')


def main():
    mybot = Updater(settings.API_KEY, use_context=True) 

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', name_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()