import lcddriver
from time import *

lcd = lcddriver.lcd()
lcd.lcd_clear()

lcd.lcd_display_string("Init 1", 1)
lcd.lcd_display_string("Init 2",2)
