from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import dweepy

datos=dweepy.get_latest_dweet_for('TesisTonnyAlvarado')
# print datos[0]['content']['presion']
print 'Presion = %6f bares'%(datos[0]['content']['presion'])
print 'Flujo = %6f m/s'%(datos[0]['content']['flujo'])
print 'Nivel = %6f in'%(datos[0]['content']['nivel'])
