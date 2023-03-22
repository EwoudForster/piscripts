import time 
import wiringpi 
import sys

pin = [2,3,4,6]

def blink():
    #1 and 3
    first = [0,2]
    last = [1,3]
    for i in range(0,2):
        wiringpi.digitalWrite(pin[first[i]], 1) 
    time.sleep(0.1)  
    
    for i in range(0,2):
        wiringpi.digitalWrite(pin[first[i]], 0) 
    time.sleep(0.1)
    #2 and 4

    time.sleep(1)
    for i in range(0,2):
        wiringpi.digitalWrite(pin[last[i]], 1) 
    time.sleep(0.1)

    for i in range(0,2):
        wiringpi.digitalWrite(pin[last[i]], 0) 
    
    time.sleep(1)

#SETUP
print("Start") 

wiringpi.wiringPiSetup() 
for i in range(0,4):
    wiringpi.pinMode(pin[i], 1) 

#MAIN
while True: 
    blink()