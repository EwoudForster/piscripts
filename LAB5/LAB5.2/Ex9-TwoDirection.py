import time 
import wiringpi 
import sys

stepperPins = [2,3,4,6] 
stepperPinsReverse = [6,4,3,2]
switchPins = [9, 10]
def Controlmode():
    while True:
        if (wiringpi.digitalRead(switchPins[0]) == 0):
            print("Motor turning Clockwise")
            time.sleep (0.3) 
            for pinStepper in stepperPins:
                wiringpi.digitalWrite(pinStepper, 1)
                time.sleep(0.01) # shorter delay time
                wiringpi.digitalWrite(pinStepper, 0)
                time.sleep(0.01) # shorter delay time
        elif(wiringpi.digitalRead(switchPins[1]) == 0):
            
            print("Motor turning Counter-Clockwise")
            time.sleep (0.3) 
            for pinStepper in stepperPinsReverse:
                wiringpi.digitalWrite(pinStepper, 0)
                time.sleep(0.01) # shorter delay time
                wiringpi.digitalWrite(pinStepper, 1)
                time.sleep(0.01) # shorter delay time
        else:
             time.sleep(1)
             print("Idle")

# SETUP
print("Start") 


wiringpi.wiringPiSetup ()
for pinStepper in stepperPins:
    wiringpi.pinMode(pinStepper, 1)
for pinSwitch in switchPins:
    wiringpi.pinMode(pinSwitch, 0)
#MAIN
while True: 
    Controlmode()