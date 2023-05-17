import time 
import wiringpi 
import sys

pin = [2,3,4,6]
pinSwitch = 1

def blinkToright():
    #Left to right
    for i in range(0,4):
        wiringpi.digitalWrite(pin[i], 1) 
        time.sleep(0.1)
    
    for i in range(0,4):
        wiringpi.digitalWrite(pin[i], 0) 
        time.sleep(0.1)

def blinkToleft(): 
    Reversed = [3,2,1,0]
    for i in range(0,4):
        wiringpi.digitalWrite(pin[Reversed[i]], 1) 
        time.sleep(0.1)

    for i in range(0,4):
        wiringpi.digitalWrite(pin[Reversed[i]], 0) 
        time.sleep(0.1)

#SETUP
print("Start") 

wiringpi.wiringPiSetup() 
for i in range(0,4):
    wiringpi.pinMode(pin[i], 1) 
wiringpi.pinMode(pinSwitch, 0)

#MAIN
while True: 
    if(wiringpi.digitalRead(pinSwitch) == 1):
        print("->left")
        time.sleep(0.3)
        blinkToleft()
        

    else:
        print("->right")
        time.sleep(0.3)
        blinkToright()
        