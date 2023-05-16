import wiringpi as wp
import time

# set pin numbers
LED_PIN = 2

# initialize WiringPi
wp.wiringPiSetup()

# set up LED pin as output
wp.pinMode(LED_PIN, wp.OUTPUT)

# blinking function
def blink(pin, numberBlinks, periode, dutyCycle):
    timeHigh = periode * dutyCycle/100
    timeLow = periode - timeHigh
    for i in range(numberBlinks):
        wp.digitalWrite(pin, wp.HIGH)
        time.sleep(timeHigh)
        wp.digitalWrite(pin, wp.LOW)
        time.sleep(timeLow)

# blink LED 10 times
blink(LED_PIN, 20, 0.5, 30)

# cleanup
print("program executed")
