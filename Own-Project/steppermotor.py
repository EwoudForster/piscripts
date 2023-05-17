# lab 5.2 ex8 + ex 7
import time 
import wiringpi 
import sys

stepperPins = [16,6,4,3]

def Close(amount):

    for j in range(amount):
        for i in range(4):
            wiringpi.digitalWrite(stepperPins[i], 1)
            time.sleep(0.01)
            wiringpi.digitalWrite(stepperPins[i], 0)
            time.sleep(0.01) 
    return "Close"

def Reset(amount):

    reversedPins = stepperPins[::-1]
    for j in range(amount):
        for i in range(4):
            wiringpi.digitalWrite(reversedPins[i], 1)
            time.sleep(0.01)
            wiringpi.digitalWrite(reversedPins[i], 0)
            time.sleep(0.01)
            
    return "Reset"

def Setup():
    # SETUP
    wiringpi.wiringPiSetup() 
    for pinStepper in stepperPins:
        wiringpi.pinMode(pinStepper, 1) 
