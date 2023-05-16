#LAB 5.2 ex 2
import time
import wiringpi
import sys
  
def check():
    #Setup
    pinSwitch = [5,7]
    pin = 2
    wiringpi.wiringPiSetup()
    for switch in pinSwitch:
        wiringpi.pinMode(switch, 0)
    if(wiringpi.digitalRead(pinSwitch[0]) == 1 and wiringpi.digitalRead(pinSwitch[1]) == 1):
        return "nothing"
    elif(wiringpi.digitalRead(pinSwitch[0]) == 1):
        return "close"
        time.sleep(1)

    elif(wiringpi.digitalRead(pinSwitch[1]) == 1):
        return "reset"
        time.sleep(1)
