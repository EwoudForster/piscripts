# https://thomasmore.instructure.com/courses/26527/files/5601601?module_item_id=1814743 
import time
import wiringpi
import spidev
from ClassLCD import LCD


def ActivateLCD():
        wiringpi.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
        time.sleep(0.000005)

def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)
    lcd_1 = LCD(PIN_OUT)
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(0)
    DeactivateLCD()

PIN_OUT     =   {  
                    'SCLK'  :   14,
                    'DIN'   :   11,
                    'DC'    :   9, 
                    'CS'    :   15, #We will not connect this pin! --> we use w13
                    'RST'   :   10,
                    'LED'   :   6, #backlight   
    }
pin_CS_lcd = 13
def setup():
    wiringpi.wiringPiSetup() 
    wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0)  #(channel, port, speed, mode)
    wiringpi.pinMode(pin_CS_lcd , 1)            # Set pin to mode 1 ( OUTPUT )
    ActivateLCD()
    
def LCD_output(string):
        
    
    #IN THIS CODE WE USE W13 (PIN 22) AS CHIP SELECT
   
    
    lcd_1 = LCD(PIN_OUT)
    lcd_1.clear()
    lcd_1.set_backlight(1)
    ActivateLCD()
    lcd_1.clear()
    lcd_1.go_to_xy(0, 0)
    lcd_1.put_string(string)
    lcd_1.refresh()