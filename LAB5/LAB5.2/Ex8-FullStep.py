import time 
import wiringpi 
import sys

stepperPins = [2,3,4,6]

def fulldrive():
    for i in range(4):
        wiringpi.digitalWrite(stepperPins[i], 1)
        time.sleep(0.01)
        wiringpi.digitalWrite(stepperPins[i], 0)
        time.sleep(0.01)
        wiringpi.digitalWrite(stepperPins[(i+1)%4], 1)
        time.sleep(0.01) 

# SETUP
print("Start") 

wiringpi.wiringPiSetup() 
for pinStepper in stepperPins:
    wiringpi.pinMode(pinStepper, 1) 

#MAIN
while True: 
    fulldrive()