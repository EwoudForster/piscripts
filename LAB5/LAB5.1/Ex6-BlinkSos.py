import time 
import wiringpi 
import sys

pin = [2,3,4,6]

def blink():
    sosSignal = [0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5]
    for i in range(0,8):
        wiringpi.digitalWrite(pin[0], 1) 
        time.sleep(sosSignal[i]) 
        wiringpi.digitalWrite(pin[0], 0)
        time.sleep(0.4) 


#SETUP
print("Start") 

wiringpi.wiringPiSetup() 
for i in range(0,4):
    wiringpi.pinMode(pin[i], 1) 

#MAIN
while True: 
    blink()