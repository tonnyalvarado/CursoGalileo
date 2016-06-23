from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import pyupm_grove as grove

light = GroveLight(0)

def iniciar(bot,update):
	bot.sendMessage(update.message.chat_id,text='Hola, bienvenido!')

def obtenluz(bot,update):
	luz = light.value()
	bot.sendMessage(update.message.chat_id,text='Luz: %6d'%luz)

def echo(bot,update):
	bot.sendMessage(update.message.chat_id,text=update.message.text)

def error(bot,update,error):
	print 'La actualizacion "%s" causo el error "%s"'%(update,error)

updater = Updater("236717193:AAGvObsy9lyXSuWMTQjuaIvYR8aZK3m1Bvc")

dp = updater.dispatcher

dp.add_handler(CommandHandler("start",iniciar))
dp.add_handler(CommandHandler("luz",obtenluz))

dp.add_handler(MessageHandler([Filters.text],echo))

dp.add_error_handler(error)

updater.start_polling()

updater.idle()
