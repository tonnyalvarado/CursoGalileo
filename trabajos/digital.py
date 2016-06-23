import mraa
import time
import pyupm_i2clcd as lcd

myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

led = mraa.Gpio(13)
pin2 = mraa.Gpio(2)
pin4 = mraa.Gpio(4)
pin2.dir(mraa.DIR_IN)
pin4.dir(mraa.DIR_IN)
led.dir(mraa.DIR_OUT)

while True:
	entrada1 = pin2.read()
	entrada2 = pin4.read()
	salida =(entrada1 and entrada2)
	myLcd.clear()
	if salida == 1:
		myLcd.setCursor(0,0)
		myLcd.setColor(255,0,0)
		myLcd.write('Led:')
		myLcd.setCursor(1,0)
		myLcd.write("Encendido")
	else:
		myLcd.setCursor(0,0)
		myLcd.setColor(0,0,255)
		myLcd.write('Led:')
		myLcd.setCursor(1,0)
		myLcd.write("Apagado")
	led.write(salida)
	time.sleep(1)
