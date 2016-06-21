#!/usr/bin/python
import time
import sys
import signal
def manejadordesenal(signal,frame):
	sys.exit(0)

signal.signal(signal.SIGINT,manejadordesenal)
while(True):
	print "Hola, desde el curso de intel Galileo"
	time.sleep(2)
#fin
