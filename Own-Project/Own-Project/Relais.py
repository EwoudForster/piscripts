# Lab5.2 ec 6
import time
import wiringpi

# Setup
relaisPins = [8]
def Setup():
    wiringpi.wiringPiSetup()
    for pinRelais in relaisPins:
        wiringpi.pinMode(pinRelais, 1)

def NotCaught():
    wiringpi.digitalWrite(relaisPins[0], 1)

def Caught():
    wiringpi.digitalWrite(relaisPins[0], 0)