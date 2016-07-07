from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import time

light = grove.GroveLight(0)
temp = grove.GroveTemp(1)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

rojo = 0
verde = 0
azul = 122

myLcd.setCursor(0,0)
myLcd.setColor(rojo,verde,azul)

# Definimos manejadores de comandos. Toman normalmente dos argumentos: bot y
# update. Los manejadores de errores tambien reciben un objeto TelegramError 
#que contienen informacion del error.
def iniciar(bot, update):
    myLcd.write('Hola, bienvenido')
    bot.sendMessage(update.message.chat_id, text='Hola, bienvenido!')

def obtenluz(bot, update):
    luz = light.value()
    bot.sendMessage(update.message.chat_id, text='Luz=%6d'% 
luz)

def obtentemp(bot, update):
    temperatura = temp.value()
    bot.sendMessage(update.message.chat_id,text='Temperatura=%6d'%temperatura)

def cambiacolor(rojo,verde,azul):
    myLcd.setColor(rojo,verde,azul)

#Manejador de mensajes, en el ejemplo simplemente repite el mensaje 
#recibido
def echo(bot, update):
    myLcd.clear()
    myLcd.setCursor(0,0)
    myLcd.write(str(update.message.text))
    bot.sendMessage(update.message.chat_id, text=update.message.text)

#Manejador de errores	
def error(bot, update, error):
    print 'La actualizacion "%s" causo el error "%s"' % (update, error)

# Creamos el Manejador de Eventos y le pasamos el token del bot.
updater = Updater("236717193:AAGvObsy9lyXSuWMTQjuaIvYR8aZK3m1Bvc")

# Obtenemos una referencia al dispatcher para registrar nuestros 
#manejadores|
dp = updater.dispatcher

# registramos manejadores
dp.add_handler(CommandHandler("start", iniciar))
dp.add_handler(CommandHandler("luz", obtenluz))
dp.add_handler(CommandHandler("temperatura", obtentemp))
dp.add_handler(CommandHandler(li=["color",r,v,a],cambiacolor(li[1],li[2],li[3])))

# registramos que hacer con los mensajes
dp.add_handler(MessageHandler([Filters.text], echo))

# Manejador de errores
dp.add_error_handler(error)

# Iniciamos el Bot
updater.start_polling()

# Se ejecuta el bot hasta que se presiona Ctrl-C o el proceso recibe 
#SIGINT,
# SIGTERM o SIGABRT. Esto debe ser ejecutado la mayoria de las veces, 
#pues
# start_polling() es no bloqueante y detendra el bot elegantemente.
updater.idle()

