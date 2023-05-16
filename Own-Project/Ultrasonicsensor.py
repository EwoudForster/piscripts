# Code lab 5 button code
# lab 5 powerpoint
import time
import wiringpi
import sys

TRIG = 2
ECHO = 1

def setup():
    #Setup

    wiringpi.wiringPiSetup()
    wiringpi.pinMode(TRIG, 1)
    wiringpi.pinMode(ECHO, 0)


def distance():
    wiringpi.digitalWrite(TRIG, 1)
    time.sleep(0.00001)
    wiringpi.digitalWrite(TRIG, 0)

    signal_high  = time.time()
    while wiringpi.digitalRead(ECHO) == 0:
        signal_high  = time.time()

    signal_low  = time.time()
    while wiringpi.digitalRead(ECHO) == 1:
        signal_low  = time.time()
        
    timepassed = signal_low - signal_high
    distance = timepassed * 17000
    distance = round(distance, 2)
    return distance

    