from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
import pyupm_grove as grove

light = grove.GroveLight(0)

def iniciar(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hola, bienvenido!')

def obtenluz(bot, update):
    luz = light.value()
    bot.sendMessage(update.message.chat_id, text='Luz=%6d'% luz)

#Manejador de mensajes, en el ejemplo simplemente repite el mensaje recibido
def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

#Manejador de errores	
def error(bot, update, error):
    print 'La actualizacion "%s" causo el error "%s"' % (update, error)

# Creamos el Manejador de Eventos y le pasamos el token del bot.
updater = Updater("236717193:AAGvObsy9lyXSuWMTQjualvYR8aZK3m1Bvc")

# Obtenemos una referencia al dispatcher para registrar nuestros manejadores|
dp = updater.dispatcher

# registramos manejadores
dp.add_handler(CommandHandler("start", iniciar))
dp.add_handler(CommandHandler("luz", obtenluz))

# registramos que hacer con los mensajes
dp.add_handler(MessageHandler([Filters.text], echo))

# Manejador de errores
dp.add_error_handler(error)

# Iniciamos el Bot
updater.start_polling()

# Se ejecuta el bot hasta que se presiona Ctrl-C o el proceso recibe SIGINT,
# SIGTERM o SIGABRT. Esto debe ser ejecutado la mayoria de las veces,pues
# start_polling() es no bloqueante y detendra el bot elegantemente.
updater.idle()
