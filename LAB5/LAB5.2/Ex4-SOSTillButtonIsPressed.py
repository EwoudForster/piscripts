import time
import wiringpi
import sys

def blink(_pin):
    sosSignal = [0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5]
    for i in range(0,8):
        wiringpi.digitalWrite(_pin, 1) 
        time.sleep(sosSignal[i]) 
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(0.4) 


#Setup
print("start")
pinSwitch = 1
pin = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)
wiringpi.pinMode(pinSwitch, 0)


while True:
    if(wiringpi.digitalRead(pinSwitch) == 1):
        print("led blinks")
        time.sleep(0.3)
        blink(pin)
        

    else:
        print("LED not flashing")
        time.sleep(0.3)
        wiringpi.digitalWrite(pin, 0)
        




