import time
import wiringpi
import sys

def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)
    time.sleep(0.5)
    wiringpi.digitalWrite(_pin, 0)
    time.sleep(0.5)


#Setup
print("start")
pinSwitch = 1
pin = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)
wiringpi.pinMode(pinSwitch, 0)


while True:
    if(wiringpi.digitalRead(pinSwitch) == 0):
        print("LED not flashing")
        time.sleep(0.3)
        wiringpi.digitalWrite(pin, 0)

    else:
        print("led blinks")
        time.sleep(0.3)
        blink(pin)




