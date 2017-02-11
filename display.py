import lcddriver
from time import *

lcd = lcddriver.lcd()
lcd.lcd_clear()


def writeScore(points):
    lcd.lcd_display_string(str(points),2)

def writeText(text):
    lcd.lcd_display_string(str(text), 1)