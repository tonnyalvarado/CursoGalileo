#!/usr/bin/python
import signal
import sys
import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import dweepy

def interruptHandler(signal, frame):
	sys.exit(0)

if __name__ == '__main__':
	signal.signal(signal.SIGINT, interruptHandler)
	myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
 	sensorluz = grove.GroveLight(0)
 	sensortemp = grove.GroveTemp(1)
	colorR = 0;
 	colorG = 255;
 	colorB = 0;
 	myLcd.setColor(colorR,colorG,colorB)
 	# Read the input and print, waiting 1/2 second between
	# readings
	myLcd.setCursor(0,0)
	myLcd.write('Luz:')
	myLcd.setCursor(1,0)
	myLcd.write('Temperatura:')
 	while True:
 		valorSensorL = sensorluz.value();
		valorSensorT = sensortemp.value()
 		myLcd.setCursor(0,4)		
 		myLcd.write('%3d'% valorSensorL)
		myLcd.setCursor(1,12)
		myLcd.write('%3d'%valorSensorT)
 		datos = {"Luz":valorSensorL , "Temperatura": 
valorSensorT}
		dweepy.dweet_for("GalileoTonnyAlvarado",datos)
		time.sleep(2)
 	del sensorluz
