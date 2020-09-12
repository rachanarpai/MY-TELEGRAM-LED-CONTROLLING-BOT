from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
from Adafruit_IO import Client, Feed, Data
import os   #Operating System Library
x = os.getenv(' ADAFRUIT_IO_USERNAME')     #ADAFRUIT_IO_USERNAME
y = os.getenv('ADAFRUIT_IO_KEY')    # ADAFRUIT_IO_KEY
z = os.getenv('TELEGRAM_BOT_TOKEN')  # TELEGRAM_BOT_TOKEN
aio = Client(x,y)

def start(bot,update):
    chat_id=update.message.chat_id
    bot.send_message(chat_id,text='''This bot sends data to adafruit for turning on or off the LED...,please type
    1- (/turnon,/TOn,/On) to lightup the LED .
    2- (/turnoff,/TOff,/Off) to put down the LED.
                thanks''')

def on(bot,update):
    chat_id=update.message.chat_id
    bot.send_message(chat_id,text="Led is on")
    bot.send_photo(chat_id,photo='https://cdn1.vectorstock.com/i/1000x1000/59/15/bulb-light-icon-line-lamp-on-symbol-vector-21085915.jpg')
    value=Data(value=1)
    value_send=aio.create_data('BOT',value)


def off(bot,update):
    chat_id=update.message.chat_id
    bot.send_message(chat_id,text="Led is off")
    bot.send_photo(chat_id,photo='https://cdn5.vectorstock.com/i/1000x1000/59/14/bulb-light-icon-line-idea-symbol-vector-21085914.jpg')
    value=Data(value=0)
    value_send=aio.create_data('BOT',value)

def inmes(bot,update):
    mess_text=update.message.text
    if mess_text=='turnon':
      on(bot,update)

    elif mess_text=='TOn':
      on(bot,update)

    elif mess_text=='On':
      on(bot,update)
   
    elif mess_text=='turnoff':
      off(bot,update)

    elif mess_text=='TOff':
      off(bot,update)
   
    elif mess_text=='Off':
      off(bot,update)
  


u = Updater(z)
dp=u.dispatcher
dp.add_handler(CommandHandler('start',start))
dp.add_handler(CommandHandler('turnon',on))
dp.add_handler(CommandHandler('TOn',on))
dp.add_handler(CommandHandler('On',on))
dp.add_handler(CommandHandler('turnoff',off))
dp.add_handler(CommandHandler('TOff',off))
dp.add_handler(CommandHandler('Off',off))
dp.add_handler(MessageHandler(Filters.text & (~Filters.command),inmes))
u.start_polling()
u.idle() 
