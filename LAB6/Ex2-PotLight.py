import wiringpi
import time

def ActivateADC ():
    wiringpi.digitalWrite(pin_CS_adc, 0)       # Actived ADC using CS
    time.sleep(0.000005)


def DeactivateADC():
    wiringpi.digitalWrite(pin_CS_adc, 1)       # Deactived ADC using CS
    time.sleep(0.000005)


def readadc(adcnum): 
    if ((adcnum > 7) or (adcnum < 0)): 
        return -1 
    revlen, recvData = wiringpi.wiringPiSPIDataRW(1, bytes([1,(8+adcnum)<<4,0]))
    time.sleep(0.000005)
    adcout = ((recvData[1]&3) << 8) + recvData[2] 
    
    return adcout  

#Setup
pin_CS_adc = 16                                 #We will use w16 as CE, not the default pin w15!
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin_CS_adc, 1)                 # Set ce to mode 1 ( OUTPUT )
wiringpi.wiringPiSPISetupMode(1, 0, 500000, 0)  #(channel, port, speed, mode)

pins = [2,3]
wiringpi.wiringPiSetup() 
for pin in pins:
    wiringpi.pinMode(pin, 1)  #setting up the lightpins

#Main
try:
    while True:
        ActivateADC()
        tmp0 = readadc(0) # read channel 0
        
        DeactivateADC()
        ActivateADC()
        tmp1 = readadc(1)
        DeactivateADC()
        print ("input0:",tmp0, "input1:", tmp1)

        if tmp0 < tmp1: #if the first potmeter is more than the second one, the first light goes on
            wiringpi.digitalWrite(pins[0], 1)  
            wiringpi.digitalWrite(pins[1], 0)


        elif tmp0 > tmp1:  #if the second potmeter is more than the first one, the second light goes on
            wiringpi.digitalWrite(pins[1], 1)
            wiringpi.digitalWrite(pins[0], 0)

        else:  #if the both potmeters are equal then both lights are off
            wiringpi.digitalWrite(pins[0], 0)
            wiringpi.digitalWrite(pins[1], 0)

        time.sleep(0.2)

except KeyboardInterrupt:
    DeactivateADC()
    print("\nProgram terminated")

    