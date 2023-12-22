import board
import digitalio
import busio

import adafruit_platformdetect.constants.boards as ap_board
from adafruit_blinka.agnostic import board_id, detector


print("Hello blinka!")
print("Board id is: ",board_id)

try:
    # Try to great a Digital input
    pin = digitalio.DigitalInOut(board.PA6) #not needed now
    print("Digital IO ok!")
except Exception as e:
    print(e)

# Try to create an I2C device
try:
    i2c = busio.I2C(board.I2C2_SCL_M0, board.I2C2_SDA_M0)
    print("I2C default 2 ok!")
except Exception as e:
    print(e)

# Try to create an SPI device
try:
    spi = busio.SPI(board.SCLK, board.MOSI, board.MISO) 
    print("SPI ok!")
except:
    pass
print("done!")