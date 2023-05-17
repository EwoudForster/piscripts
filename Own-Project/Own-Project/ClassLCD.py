# https://thomasmore.instructure.com/courses/26527/files/5601600?module_item_id=1814742
import time
import wiringpi
import spidev

pi_logo = [
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF8, 0xF8, 0xFC, 0xAE, 0x0E, 0x0E, 0x06, 0x0E, 0x06, 
    0xCE, 0x86, 0x8E, 0x0E, 0x0E, 0x1C, 0xB8, 0xF0, 0xF8, 0x78, 0x38, 0x1E, 0x0E, 0x8E, 0x8E, 0xC6, 
    0x0E, 0x06, 0x0E, 0x06, 0x0E, 0x9E, 0xFE, 0xFC, 0xF8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x0F, 0x0F, 0xFE, 
    0xF8, 0xF0, 0x60, 0x60, 0xE0, 0xE1, 0xE3, 0xF7, 0x7E, 0x3E, 0x1E, 0x1F, 0x1F, 0x1F, 0x3E, 0x7E, 
    0xFB, 0xF3, 0xE1, 0xE0, 0x60, 0x70, 0xF0, 0xF8, 0xBE, 0x1F, 0x0F, 0x07, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xC0, 
    0xE0, 0xFC, 0xFE, 0xFF, 0xF3, 0x38, 0x38, 0x0C, 0x0E, 0x0F, 0x0F, 0x0F, 0x0E, 0x3C, 0x38, 0xF8, 
    0xF8, 0x38, 0x3C, 0x0E, 0x0F, 0x0F, 0x0F, 0x0E, 0x0C, 0x38, 0x38, 0xF3, 0xFF, 0xFF, 0xF8, 0xE0, 
    0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x7F, 0xFF, 0xE7, 0xC3, 0xC1, 0xE0, 0xFF, 0xFF, 0x78, 0xE0, 0xC0, 0xC0, 0xC0, 0xC0, 0xE0, 
    0x60, 0x78, 0x38, 0x3F, 0x3F, 0x38, 0x38, 0x60, 0x60, 0xC0, 0xC0, 0xC0, 0xC0, 0xE0, 0xF8, 0x7F, 
    0xFF, 0xE0, 0xC1, 0xC3, 0xE7, 0x7F, 0x3E, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x0F, 0x7F, 0xFF, 0xF1, 0xE0, 0xC0, 0x80, 0x01, 
    0x03, 0x9F, 0xFF, 0xF0, 0xE0, 0xE0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xE0, 0xE0, 0xF0, 0xFF, 0x9F, 
    0x03, 0x01, 0x80, 0xC0, 0xE0, 0xF1, 0x7F, 0x1F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 
    0x03, 0x03, 0x07, 0x07, 0x0F, 0x1F, 0x1F, 0x3F, 0x3B, 0x71, 0x60, 0x60, 0x60, 0x60, 0x60, 0x71, 
    0x3B, 0x1F, 0x0F, 0x0F, 0x0F, 0x07, 0x03, 0x03, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
]


# font5x7
font5x7 = {
  'HEIGHT'  : 7,

  ' ' : {'byte' : [0x00, 0x00, 0x00, 0x00, 0x00], 'width' : 5},
  '!' : {'byte' : [0x00, 0x00, 0x5f, 0x00, 0x00], 'width' : 5},
  '"' : {'byte' : [0x00, 0x07, 0x00, 0x07, 0x00], 'width' : 5},
  '#' : {'byte' : [0x14, 0x7f, 0x14, 0x7f, 0x14], 'width' : 5},
  '$' : {'byte' : [0x24, 0x2a, 0x7f, 0x2a, 0x12], 'width' : 5},
  '%' : {'byte' : [0x23, 0x13, 0x08, 0x64, 0x62], 'width' : 5},
  '&' : {'byte' : [0x36, 0x49, 0x55, 0x22, 0x50], 'width' : 5},
  "'" : {'byte' : [0x00, 0x05, 0x03, 0x00, 0x00], 'width' : 5},
  '(' : {'byte' : [0x00, 0x1c, 0x22, 0x41, 0x00], 'width' : 5},
  ')' : {'byte' : [0x00, 0x41, 0x22, 0x1c, 0x00], 'width' : 5},
  '*' : {'byte' : [0x14, 0x08, 0x3e, 0x08, 0x14], 'width' : 5},
  '+' : {'byte' : [0x08, 0x08, 0x3e, 0x08, 0x08], 'width' : 5},
  ',' : {'byte' : [0x00, 0x50, 0x30, 0x00, 0x00], 'width' : 5},
  '-' : {'byte' : [0x08, 0x08, 0x08, 0x08, 0x08], 'width' : 5},
  '.' : {'byte' : [0x00, 0x60, 0x60, 0x00, 0x00], 'width' : 5},
  '/' : {'byte' : [0x20, 0x10, 0x08, 0x04, 0x02], 'width' : 5},
  '0' : {'byte' : [0x3e, 0x51, 0x49, 0x45, 0x3e], 'width' : 5},
  '1' : {'byte' : [0x00, 0x42, 0x7f, 0x40, 0x00], 'width' : 5},
  '2' : {'byte' : [0x42, 0x61, 0x51, 0x49, 0x46], 'width' : 5},
  '3' : {'byte' : [0x21, 0x41, 0x45, 0x4b, 0x31], 'width' : 5},
  '4' : {'byte' : [0x18, 0x14, 0x12, 0x7f, 0x10], 'width' : 5},
  '5' : {'byte' : [0x27, 0x45, 0x45, 0x45, 0x39], 'width' : 5},
  '6' : {'byte' : [0x3c, 0x4a, 0x49, 0x49, 0x30], 'width' : 5},
  '7' : {'byte' : [0x01, 0x71, 0x09, 0x05, 0x03], 'width' : 5},
  '8' : {'byte' : [0x36, 0x49, 0x49, 0x49, 0x36], 'width' : 5},
  '9' : {'byte' : [0x06, 0x49, 0x49, 0x29, 0x1e], 'width' : 5},
  ':' : {'byte' : [0x00, 0x36, 0x36, 0x00, 0x00], 'width' : 5},
  ';' : {'byte' : [0x00, 0x56, 0x36, 0x00, 0x00], 'width' : 5},
  '<' : {'byte' : [0x08, 0x14, 0x22, 0x41, 0x00], 'width' : 5},
  '=' : {'byte' : [0x14, 0x14, 0x14, 0x14, 0x14], 'width' : 5},
  '>' : {'byte' : [0x00, 0x41, 0x22, 0x14, 0x08], 'width' : 5},
  '?' : {'byte' : [0x02, 0x01, 0x51, 0x09, 0x06], 'width' : 5},
  '@' : {'byte' : [0x32, 0x49, 0x79, 0x41, 0x3e], 'width' : 5},
  'A' : {'byte' : [0x7e, 0x11, 0x11, 0x11, 0x7e], 'width' : 5},
  'B' : {'byte' : [0x7f, 0x49, 0x49, 0x49, 0x36], 'width' : 5},
  'C' : {'byte' : [0x3e, 0x41, 0x41, 0x41, 0x22], 'width' : 5},
  'D' : {'byte' : [0x7f, 0x41, 0x41, 0x22, 0x1c], 'width' : 5},
  'E' : {'byte' : [0x7f, 0x49, 0x49, 0x49, 0x41], 'width' : 5},
  'F' : {'byte' : [0x7f, 0x09, 0x09, 0x09, 0x01], 'width' : 5},
  'G' : {'byte' : [0x3e, 0x41, 0x49, 0x49, 0x7a], 'width' : 5},
  'H' : {'byte' : [0x7f, 0x08, 0x08, 0x08, 0x7f], 'width' : 5},
  'I' : {'byte' : [0x00, 0x41, 0x7f, 0x41, 0x00], 'width' : 5},
  'J' : {'byte' : [0x20, 0x40, 0x41, 0x3f, 0x01], 'width' : 5},
  'K' : {'byte' : [0x7f, 0x08, 0x14, 0x22, 0x41], 'width' : 5},
  'L' : {'byte' : [0x7f, 0x40, 0x40, 0x40, 0x40], 'width' : 5},
  'M' : {'byte' : [0x7f, 0x02, 0x0c, 0x02, 0x7f], 'width' : 5},
  'N' : {'byte' : [0x7f, 0x04, 0x08, 0x10, 0x7f], 'width' : 5},
  'O' : {'byte' : [0x3e, 0x41, 0x41, 0x41, 0x3e], 'width' : 5},
  'P' : {'byte' : [0x7f, 0x09, 0x09, 0x09, 0x06], 'width' : 5},
  'Q' : {'byte' : [0x3e, 0x41, 0x51, 0x21, 0x5e], 'width' : 5},
  'R' : {'byte' : [0x7f, 0x09, 0x19, 0x29, 0x46], 'width' : 5},
  'S' : {'byte' : [0x46, 0x49, 0x49, 0x49, 0x31], 'width' : 5},
  'T' : {'byte' : [0x01, 0x01, 0x7f, 0x01, 0x01], 'width' : 5},
  'U' : {'byte' : [0x3f, 0x40, 0x40, 0x40, 0x3f], 'width' : 5},
  'V' : {'byte' : [0x1f, 0x20, 0x40, 0x20, 0x1f], 'width' : 5},
  'W' : {'byte' : [0x3f, 0x40, 0x38, 0x40, 0x3f], 'width' : 5},
  'X' : {'byte' : [0x63, 0x14, 0x08, 0x14, 0x63], 'width' : 5},
  'Y' : {'byte' : [0x07, 0x08, 0x70, 0x08, 0x07], 'width' : 5},
  'Z' : {'byte' : [0x61, 0x51, 0x49, 0x45, 0x43], 'width' : 5},
  '[' : {'byte' : [0x00, 0x7f, 0x41, 0x41, 0x00], 'width' : 5},
  '\\': {'byte' : [0x02, 0x04, 0x08, 0x10, 0x20], 'width' : 5},
  ']' : {'byte' : [0x00, 0x41, 0x41, 0x7f, 0x00], 'width' : 5},
  '^' : {'byte' : [0x04, 0x02, 0x01, 0x02, 0x04], 'width' : 5},
  '_' : {'byte' : [0x40, 0x40, 0x40, 0x40, 0x40], 'width' : 5},
  '`' : {'byte' : [0x00, 0x01, 0x02, 0x04, 0x00], 'width' : 5},
  'a' : {'byte' : [0x20, 0x54, 0x54, 0x54, 0x78], 'width' : 5},
  'b' : {'byte' : [0x7f, 0x48, 0x44, 0x44, 0x38], 'width' : 5},
  'c' : {'byte' : [0x38, 0x44, 0x44, 0x44, 0x20], 'width' : 5},
  'd' : {'byte' : [0x38, 0x44, 0x44, 0x48, 0x7f], 'width' : 5},
  'e' : {'byte' : [0x38, 0x54, 0x54, 0x54, 0x18], 'width' : 5},
  'f' : {'byte' : [0x08, 0x7e, 0x09, 0x01, 0x02], 'width' : 5},
  'g' : {'byte' : [0x0c, 0x52, 0x52, 0x52, 0x3e], 'width' : 5},
  'h' : {'byte' : [0x7f, 0x08, 0x04, 0x04, 0x78], 'width' : 5},
  'i' : {'byte' : [0x00, 0x44, 0x7d, 0x40, 0x00], 'width' : 5},
  'j' : {'byte' : [0x20, 0x40, 0x44, 0x3d, 0x00], 'width' : 5},
  'k' : {'byte' : [0x7f, 0x10, 0x28, 0x44, 0x00], 'width' : 5},
  'l' : {'byte' : [0x00, 0x41, 0x7f, 0x40, 0x00], 'width' : 5},
  'm' : {'byte' : [0x7c, 0x04, 0x18, 0x04, 0x78], 'width' : 5},
  'n' : {'byte' : [0x7c, 0x08, 0x04, 0x04, 0x78], 'width' : 5},
  'o' : {'byte' : [0x38, 0x44, 0x44, 0x44, 0x38], 'width' : 5},
  'p' : {'byte' : [0x7c, 0x14, 0x14, 0x14, 0x08], 'width' : 5},
  'q' : {'byte' : [0x08, 0x14, 0x14, 0x18, 0x7c], 'width' : 5},
  'r' : {'byte' : [0x7c, 0x08, 0x04, 0x04, 0x08], 'width' : 5},
  's' : {'byte' : [0x48, 0x54, 0x54, 0x54, 0x20], 'width' : 5},
  't' : {'byte' : [0x04, 0x3f, 0x44, 0x40, 0x20], 'width' : 5},
  'u' : {'byte' : [0x3c, 0x40, 0x40, 0x20, 0x7c], 'width' : 5},
  'v' : {'byte' : [0x1c, 0x20, 0x40, 0x20, 0x1c], 'width' : 5},
  'w' : {'byte' : [0x3c, 0x40, 0x30, 0x40, 0x3c], 'width' : 5},
  'x' : {'byte' : [0x44, 0x28, 0x10, 0x28, 0x44], 'width' : 5},
  'y' : {'byte' : [0x0c, 0x50, 0x50, 0x50, 0x3c], 'width' : 5},
  'z' : {'byte' : [0x44, 0x64, 0x54, 0x4c, 0x44], 'width' : 5},
  '{' : {'byte' : [0x00, 0x08, 0x36, 0x41, 0x00], 'width' : 5},
  '|' : {'byte' : [0x00, 0x00, 0x7f, 0x00, 0x00], 'width' : 5},
  '}' : {'byte' : [0x00, 0x41, 0x36, 0x08, 0x00], 'width' : 5},
  '~' : {'byte' : [0x10, 0x08, 0x08, 0x10, 0x08], 'width' : 5},
}

# bit hacks
def _BV(x):
    return (0x01 << (x))

# White backlight
#CONTRAST        =   0xaa
#CONTRAST        =   0x7f
CONTRAST        =   0x48 # 0x48 gives visible result
DEFAULT         =   -1
LCD_WIDTH       =   84
LCD_HEIGHT      =   48
ROWS            =   6
COLUMNS         =   14
PIXELS_PER_ROW  =   6
ON              =   1
OFF             =   0
BLACK           =   1 # original 1
WHITE           =   0 # original 0

def bit_reverse(value, width=8):
  result = 0
  for _ in range(width):
    result = (result << 1) | (value & 1)
    value >>= 1

  return result

BITREVERSE = list(map(bit_reverse, range(256)))

spi             =   spidev.SpiDev()



class LCD:

    __buffer        =   [0x00] * (ROWS * COLUMNS * PIXELS_PER_ROW)
    __cursor_x      =   0
    __cursor_y      =   0

    __font_current  =   font5x7

    def __init__(self, PIN, dev = (1,0), speed = 500000, brightness = 256, contrast = CONTRAST):
        super(LCD, self).__init__()

        # Pin configure, wiringpi. Read more at pinout.xyz or use 'gpio readall' in terminal
        self.SCLK    =   PIN['SCLK']
        self.DIN     =   PIN['DIN']
        self.DC      =   PIN['DC']
        self.SCE     =   PIN['CS']
        self.RST     =   PIN['RST']
        self.LED     =   PIN['LED']

        spi.open(dev[0],dev[1])
        spi.max_speed_hz=speed

        # Set pin directions.
        wiringpi.wiringPiSetup()
        for pin in [self.DC, self.RST]:
            wiringpi.pinMode(pin, 1)

        # Toggle RST low to reset.
        wiringpi.digitalWrite(self.RST, OFF)
        time.sleep(0.500)
        wiringpi.digitalWrite(self.RST, ON)
        # Extended mode, bias, vop, basic mode, non-inverted display.
        self.set_contrast(contrast)

        # if LED == 1 set pin mode to PWM else set it to OUT
        if self.LED == 1:
            wiringpi.pinMode(self.LED, 2)
            wiringpi.pwmWrite(self.LED,0)
        else:
            wiringpi.pinMode(self.LED, 1)
            wiringpi.digitalWrite(self.LED, OFF)

    def refresh(self):
        self.gotoxy_spi(0,0)
        time.sleep(0.1)

        wiringpi.digitalWrite(self.DC, ON)
        for byte in self.__buffer:
            spi.writebytes([byte])

    def new_line(self, font = None):
        font                =   font or self.__font_current
        self.__cursor_x     =   0
        self.__cursor_y     +=  font['HEIGHT'] + 1

    ##############################################

    def set_pixel(self, x, y, color = BLACK, toggle = False):
        if ((x >= LCD_WIDTH) or (y >= LCD_HEIGHT)):
            print('WRONG COORDINATES, x = {}, y = {}'.format(x, y))
            return

        # rather than set the pixel black or white, just invert/toggle it
        if (toggle):
            color_current = self.get_pixel(x, y)
            self.set_pixel(x, y, color = not color_current)
            return
            
        if (color == BLACK):
            self.__buffer[x + (y // 8) * LCD_WIDTH]  |=   _BV(y % 8)
        else:
            self.__buffer[x + (y // 8) * LCD_WIDTH]  &=  ~_BV(y % 8)

    def get_pixel(self, x, y):
        if ((x > LCD_WIDTH) or (y > LCD_HEIGHT)):
            return 0

        if ((x < 0) or (y < 0)):
            return 0

        return (self.__buffer[x + (y // 8) * LCD_WIDTH] >> (y % 8)) & 0x1

    def set_font(self, font):
        self.__font_current    =   font

    def go_to_xy(self, x, y):
        self.__cursor_x    =   x
        self.__cursor_y    =   y

    def put_char(self, char, x = None, y = None, font = None):

        self.__cursor_x   =   x or self.__cursor_x
        self.__cursor_y   =   y or self.__cursor_y

        # do nothing if y out of screen
        if (self.__cursor_y >= LCD_HEIGHT):
            return

        # if new line char, new line
        if (char in ['\n', '\r', '\l']):
            self.new_line(font)
            return

        try:

            font        =   font or self.__font_current
            char_width  =   font[char]['width']
            font_height =   font['HEIGHT']

            # if not enough space to write this char, new line
            if ((self.__cursor_x + char_width) >= LCD_WIDTH):
                self.new_line(font)

            # Draw the character as if it was an image
            self.draw_image(font[char]['byte'], width = char_width, height = font_height, x = self.__cursor_x, y = self.__cursor_y)

            # after writing, move the cursor to the right. Sorry, Arabic not supported :)
            self.__cursor_x    +=  char_width + 1

        except KeyError:
            pass # Ignore undefined characters.

    def put_string(self, string, x = None, y = None, font = None, is_center = False):
        font    =   font    or self.__font_current
        x       =   x       or self.__cursor_x
        y       =   y       or self.__cursor_y

        # Print the text in the center of the line
        if (is_center):
            total_width = 0
            for char in string:
                try:
                    total_width += font[char]['width'] + 1 # space between each char = 1
                except KeyError:
                    # Ignore unknown characters
                    pass

                x   =   (LCD_WIDTH - total_width) // 2 if (total_width < LCD_WIDTH) else 0

        self.go_to_xy(x, y)

        for char in string:
            self.put_char(char = char, font = font)

    ##############################################

    # Bresenham's line algorithm, thanks wikipedia
    def draw_line(self, x1, y1, x2, y2, color = BLACK):
        dx  =   abs(x2 - x1)
        dy  =   abs(y2 - y1)

        sx  =   1 if (x1 < x2) else -1
        sy  =   1 if (y1 < y2) else -1
        err =   dx - dy

        while (True):
            self.set_pixel(x1, y1, color)
            if ((x1 == x2) and (y1 == y2)):
                break

            e2  =   err * 2

            if (e2 > -dy):
                err -=  dy
                x1  +=  sx

            if (e2 < dx):
                err +=  dx
                y1  +=  sy
                
    def draw_rect(self, x1, y1, x2, y2, color = BLACK):
        self.draw_horizontal_line(x1, x2, y1, color) # upper edge
        self.draw_horizontal_line(x1, x2, y2, color) # lower edge
        self.draw_vertical_line(y1, y2, x1, color) # left edge
        self.draw_vertical_line(y1, y2, x2, color) # right edge

    # Image must be in byte array. You can convert bitmap images to byte array 
    # at http://javl.github.io/image2cpp. Thanks @javl for this useful tool
    def draw_image(self, image, width, height, x = 0, y = 0):
        for j in range(height):
            for i in range(width):
                if (image[i + (j//8)*width] & _BV(j%8)):
                    self.set_pixel(x + i, y + j)

    # An example for drawing images
    def draw_logo(self):
        self.draw_image(pi_logo, 84, 48)

    # draw multiple horizontal lines
    def fill_rect(self, x1, y1, x2, y2, color = BLACK):
        if (y1 > y2):
            y1, y2 = y2, y1
        
        for y in range(y1, y2 + 1):
            self.draw_horizontal_line(x1, x2, y, color)

    # Invert a rectangle's color
    def invert_rect(self, x1, y1, x2 = None, y2 = None, width = None, height = None):
        is_missing_parameters = ((x2 == None) or (y2 == None)) and ((width == None) or (height == None))

        if (is_missing_parameters):
            raise TypeError('draw_rect() missing one pair of parameters. You must specify x2|y2 or width|height')

        if (width != None) and (height != None):
            x2 = x1 + width
            y2 = y1 + height

        if (y1 > y2):
            y1, y2 = y2, y1

        if (x1 > x2):
            x1, x2 = x2, x1

        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                self.set_pixel(x, y, toggle = True)

    def draw_circle(self, x0, y0, radius, color = BLACK):
        f       =   1 - radius
        ddF_x   =   1
        ddF_y   =   -2 * radius
        x       =   0
        y       =   radius

        self.set_pixel(x0, y0+radius, color)
        self.set_pixel(x0, y0-radius, color)
        self.set_pixel(x0+radius, y0, color)
        self.set_pixel(x0-radius, y0, color)

        while (x < y):
            if (f >= 0):
                y       -= 1
                ddF_y   += 2
                f       += ddF_y
            
            x       += 1
            ddF_x   += 2;
            f       += ddF_x;

            self.set_pixel(x0 + x, y0 + y, color);
            self.set_pixel(x0 - x, y0 + y, color);
            self.set_pixel(x0 + x, y0 - y, color);
            self.set_pixel(x0 - x, y0 - y, color);

            self.set_pixel(x0 + y, y0 + x, color);
            self.set_pixel(x0 - y, y0 + x, color);
            self.set_pixel(x0 + y, y0 - x, color);
            self.set_pixel(x0 - y, y0 - x, color);

    def fill_circle(self, x0, y0, radius, color = BLACK):
        f       =   1 - radius
        ddF_x   =   1
        ddF_y   =   -2 * radius
        x       =   0
        y       =   radius

        for j in range (y0 - radius, y0 + radius + 1):
            self.set_pixel(x0, j, color)

        while (x < y):
            if (f >= 0):
                y       -= 1
                ddF_y   += 2 
                f       += ddF_y
            
            x       += 1
            ddF_x   += 2;
            f       += ddF_x;

            for j in range (y0 - y, y0 + y + 1):            
                self.set_pixel(x0 + x, j, color);
                self.set_pixel(x0 - x, j, color);
            
            for j in range (y0 - x, y0 + x + 1):
                self.set_pixel(x0+y, j, color);
                self.set_pixel(x0-y, j, color);

    def clear(self):
        self.go_to_xy(0,0)
        self.__buffer = [0x00] * (ROWS * COLUMNS * PIXELS_PER_ROW)

    ##############################################

    def draw_horizontal_line(self, x1, x2, y, color = BLACK):
        if (x1 > x2):
            x1, x2 = x2, x1

        for x in range(x1, x2 + 1):
            self.set_pixel(x, y, color)

    def draw_vertical_line(self, y1, y2, x, color = BLACK):
        if (y1 > y2):
            y1, y2 = y2, y1

        for y in range(y1, y2 + 1):
            self.set_pixel(x, y)

    ##############################################

    def set_backlight(self, value):
        wiringpi.digitalWrite(self.LED, value)

    # This, somehow, not functioned yet
    def set_contrast(self, contrast):

        wiringpi.digitalWrite(self.DC, OFF)
        spi.writebytes([0x21, 0x80|contrast, 0x20, 0x08|0x04])

    def gotoxy_spi(self, x, y):
        if ((0 <= x < COLUMNS) and (0 <= y < ROWS)):
            wiringpi.digitalWrite(self.DC, OFF)
            spi.writebytes([x + 128, y + 64])