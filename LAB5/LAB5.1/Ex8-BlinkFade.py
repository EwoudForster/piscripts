
import time 
import wiringpi 
import sys

pin = [2, 3, 4, 6]

def blink():
    brightness = [25, 50, 75, 100]
    wait = 0.25


    for i in range(0,4):
        wiringpi.softPwmCreate(pin[i], 0, 100)
    for i in range(0,4):
        for k in range(0,4):
            wiringpi.softPwmWrite(pin[k], brightness[i])
        time.sleep(wait)
    
    for i in range(0,4):
        wiringpi.softPwmStop(pin[i])
    time.sleep(1)


#SETUP
print("Start") 

wiringpi.wiringPiSetup() 
for i in range(0,4):
    wiringpi.pinMode(pin[i], 1) 

#MAIN
while True: 
    blink()