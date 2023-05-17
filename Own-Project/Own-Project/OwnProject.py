import time 
import wiringpi 
import sys
import LCD as screen
import steppermotor as trap
import Ultrasonicsensor as cm
import Relais as led
import threading
import CheckButton as button
import ubeac as iotsite
import Webhosting as web

exit_event = threading.Event()

time_str = ""
mouse = False
status = "Off"
count = 0


def LookingForMouse():
    screen.ActivateLCD()
    cm.setup()
    trap.Setup()
    led.Setup()
    global mouse, status, count
    minimumdistance = checkDistance()
    while not mouse:
        time.sleep(0.5)
        distance = checkDistance()
        if (button.check() == "close" or web.checkstatus() == "close" or distance + 3 < minimumdistance):
            mouse = True
            count += 1
            led.Caught()
        else:
            led.NotCaught()
            time.sleep(1)
    stepperMotor()



def checkDistance():
    time.sleep(0.5)
    distance = cm.distance()
    return distance


def stepperMotor():
    global status
    while status == "armed":
        if mouse:
            trap.Close(100)
            status = "triggered"

def LCD():
    global status, count, time_str
    while True:
        current_time = time.gmtime(time.time())
        time_str = "time: " + str(current_time.tm_hour) + ":" + str(current_time.tm_min)
        screen.LCD_output(time_str + "\nstatus: " + status + "\nnumber of triggers: " + str(count))
        time.sleep(2)


def ubeac():
    global count, status
    while True:
        iotsite.upload(status, count)
        time.sleep(2)



def Reset():
    global mouse, status, count
    mouse = False
    status = "Off"
    trap.Reset(100)
    led.NotCaught()



def program():
    global status, mouse
    while True:
        
        if status == "Off":
            led.NotCaught()
            if button.check() == "reset" or button.check() == "close" or web.checkstatus() == "arm":
                status = "armed"
                mouse = False  # Reset the mouse flag when arming

        elif status == "armed":
            if not mouse:  
                LookingForMouse()

        elif status == "triggered":
            if button.check() == "reset" or web.checkstatus() == "reset":
                Reset()



def checkstatus():
    global status
    return status


try:
    lcd = threading.Thread(target=LCD)
    websetup = threading.Thread(target=web.deploy)
    main = threading.Thread(target=program)
    online = threading.Thread(target=ubeac)
    screen.setup()
    lcd.start()
    websetup.start()
    main.start()
    online.start()



except KeyboardInterrupt:
    screen.DeactivateLCD()
    exit_event