import wiringpi as wp
import time
import bh1750

# Set up WiringPi library
wp.wiringPiSetup()

# Define GPIO ports
scl_pin = 1   # SCL = W1
sda_pin = 0   # SDA = W0

# Set up BH1750 sensor
light_sensor = bh1750.BH1750(i2c_addr=0x23, i2c_bus=1)

# Define GPIO port
gpio_pin = 1

# Set GPIO port as output
wp.pinMode(gpio_pin, wp.OUTPUT)

while True:
    # Set GPIO port output low
    wp.digitalWrite(gpio_pin, wp.LOW)

    # Wait for 0.1 seconds
    time.sleep(0.1)

    # Set GPIO port as input
    wp.pinMode(gpio_pin, wp.INPUT)

    # Wait until input on port 1 is low
    while wp.digitalRead(gpio_pin) == wp.LOW:
        pass

    # Set start time
    starttime = time.time()

    # Wait until input on port 1 is high
    while wp.digitalRead(gpio_pin) == wp.HIGH:
        pass

    # Set stop time
    stoptime = time.time()

    # Calculate interval
    interval = stoptime - starttime

    # Read light sensor value
    light_level = light_sensor.measure()

    # Print interval and light level
    print("Interval: {} s, Light level: {} lux".format(interval, light_level))
