import time 
import wiringpi 
import sys

stepperPins = [2,3,4,6]

def wavedrive():
    for pinStepper in stepperPins:
        wiringpi.digitalWrite(pinStepper, 1)
        time.sleep(0.01)
        wiringpi.digitalWrite(pinStepper, 0)
        time.sleep(0.01) 


# SETUP
print("Start") 

wiringpi.wiringPiSetup() 
for pinStepper in stepperPins:
    wiringpi.pinMode(pinStepper, 1) 

#MAIN
while True: 
    wavedrive()