from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import dweepy
import sys

def iniciar(bot, update):
	bot.sendMessage(update.message.chat_id, text='Hola, bienvenido')

def leervalores():
	try:
		datos=dweepy.get_latest_dweet_for('TesisTonnyAlvarado')
		return datos
	except:
		datos=[{'content':{"presion":0,"flujo":0.05,"nivel":10.16}}]
		return

def obtenpresion(bot, update):
    datos=leervalores()
    bot.sendMessage(update.message.chat_id, text='Presion = %6f bares'%datos[0]['content']['presion'])

def obtenflujo(bot, update):
    datos=leervalores()
    bot.sendMessage(update.message.chat_id, text='Flujo = %6f m/s'%datos[0]['content']['flujo'])

def obtennivel(bot, update):
    datos=leervalores()
    bot.sendMessage(update.message.chat_id, text='Nivel = %6f cm'%datos[0]['content']['nivel'])

def echo(bot,update):
	bot.sendMessage(update.message.chat_id, text=update.message.text)

def error(bot,update, error):
	print 'La actualizacion "%s" causo el error "%s"' % (update,error)

updater = Updater("267425517:AAEadXjXGbiVfyowX8Udi6ph_mS_qKka6_I")

dp = updater.dispatcher

dp.add_handler(CommandHandler("start",iniciar))
dp.add_handler(CommandHandler("presion",obtenpresion))
dp.add_handler(CommandHandler("flujo",obtenflujo))
dp.add_handler(CommandHandler("nivel",obtennivel))

dp.add_handler(MessageHandler([Filters.text],echo))

dp.add_error_handler(error)

updater.start_polling()

updater.idle()
