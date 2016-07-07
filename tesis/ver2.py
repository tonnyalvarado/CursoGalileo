import mraa
import time
import signal
import sys
import dweepy

def interruptHandler(signal, frame):
	sys.exit(0)

def sensorPresion():
	v = leerSensor(0)
	li = 0.0
	lf = 40.0
	return [v,li,lf] 

def sensorFlujo():
    v = leerSensor(1)
    li = 0.05
    lf = 10.0
    return [v,li,lf]

def sensorNivel():
    v = leerSensor(2)
    li = 0.0
    lf = 168.0
    return [v, li,lf]

def calculo(li):
    resultado = (((li[0]*2**12/5.0)*(100.0/2**12))/100)*(li[2]-li[1])
    return resultado + li[1]
    
def leerSensor(n):
    try:
        pinsensor = mraa.Aio(n)
        pinsensor.setBit(12)
        
        valorsensor = pinsensor.read()
        return valorsensor/819.0        
    except:
        print "Error en el conversor ADC"

if __name__ == '__main__':
    signal.signal(signal.SIGINT, interruptHandler)
    sensor = 0
    presion=0
    flujo=0
    nivel=0   
    while True:
	  myLcd.clear()      
          if sensor==0:
              presion = calculo(sensorPresion())
	      myLcd.write('Presion: %.6f'%presion)
              time.sleep(2)
          elif sensor == 1:
              flujo = calculo(sensorFlujo())
	      myLcd.write('Flujo: %.6f'%flujo)
              time.sleep(2)
          else:
              nivel = calculo(sensorNivel())
 	      myLcd.write('Nivel: %.6f'%nivel)
              time.sleep(2)
          if sensor < 2:
              sensor+=1
          else:
              sensor = 0
          datos = {"presion":presion , "flujo":flujo,"nivel":nivel}
          dweepy.dweet_for("TesisTonnyAlvarado",datos)
