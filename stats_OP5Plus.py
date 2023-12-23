################################################################################################
# stats for OrangePi 5 Plus
################################################################################################

import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import socket

from datetime import datetime, timedelta
import pytz
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

hostname = socket.gethostname()

def get_timecode_milliseconds():
    # Get the current time in UTC
    utc_now = datetime.now(pytz.utc)

    # Convert to Pacific Standard Time (PST)
    pst_timezone = pytz.timezone('America/Los_Angeles')
    pst_now = utc_now.astimezone(pst_timezone)

    # Extract the hour, minute, second, and millisecond components from the PST time
    hour = pst_now.hour
    minute = pst_now.minute
    second = pst_now.second
    millisecond = pst_now.microsecond // 1000

    # Format the components as HH:MIN:SEC:MS
    time_str = f'{hour:02d}:{minute:02d}:{second:02d}:{millisecond:03d}'

    return time_str

def display_power(disp):
    disp.poweron()
i2c = board.I2C()  # uses board.SCL and board.SDA

# Note you can change the I2C address by passing an i2c_address parameter like:
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

# 128x32 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# 128x64 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

disp.init_display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 0
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
# font = ImageFont.load_default()
# font = ImageFont.truetype('PixelOperator.ttf', 16)
font_path = os.path.join(current_directory, 'PixelOperator.ttf')
if os.path.exists(font_path):
    # The font file exists, proceed with loading the font
    font = ImageFont.truetype(font_path, 16)
else:
    # The font file does not exist in the current directory
    print("Font file 'PixelOperator.ttf' not found.")
    
# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)
# Display Refresh
LOOPTIME = 0.001666
while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    cmd = "top -bn1 | grep load | awk '{printf \"CPU: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    # MemUsage = subprocess.check_output(cmd, shell = True )
    # cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"

    Hostname = socket.gethostname()

    Disk = subprocess.check_output(cmd, shell = True )
    cmd = "sensors | grep 'Composite' | awk '{print $2}'"
    Temp = subprocess.check_output(cmd, shell = True) 
    timecode = get_timecode_milliseconds()
    
    # Pi Stats Display
    draw.text((0, 0), "IP: " + str(IP,'utf-8'), font=font, fill=255)
    draw.text((0, 16), (f'HN: {Hostname}'), font=font, fill=255)

    draw.text((0, 32), str(CPU,'utf-8') + "LA", font=font, fill=255)
    draw.text((80, 32), str(Temp,'utf-8') , font=font, fill=255)

    # draw.text((0, 32), str(MemUsage,'utf-8'), font=font, fill=255)
    #draw.text((0, 48), str(Disk,'utf-8'), font=font, fill=255)

    draw.text((0, 48),f'TC: {timecode}', font=font, fill=255)

    # # Display image
    disp.image(image)
    disp.show()
    time.sleep(LOOPTIME)


