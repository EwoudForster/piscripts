import time
import wiringpi

# Setup
print("start")
switchPins = [0, 1]
relaisPins = [2, 3]
wiringpi.wiringPiSetup()
for pinRelais in relaisPins:
    wiringpi.pinMode(pinRelais, 1)
for pinSwitch in switchPins:
    wiringpi.pinMode(pinSwitch, 0)

while True:
    if wiringpi.digitalRead(switchPins[0]) == 0:
        print("LED not flashing")
        wiringpi.digitalWrite(relaisPins[0], 0)
    elif wiringpi.digitalRead(switchPins[0]) != 0:
        print("led blinks")
        wiringpi.digitalWrite(relaisPins[0], 1)

    if wiringpi.digitalRead(switchPins[1]) == 0:
        print("LED not flashing")
        wiringpi.digitalWrite(relaisPins[1], 0)
    elif wiringpi.digitalRead(switchPins[1]) != 0:
        print("led blinks")
        wiringpi.digitalWrite(relaisPins[1], 1)
