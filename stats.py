# Created by: Michael Klements
# For Raspberry Pi Desktop Case with OLED Stats Display
# Base on Adafruit CircuitPython & SSD1306 Libraries
# Installation & Setup Instructions - https://www.the-diy-life.com/add-an-oled-stats-display-to-raspberry-pi-os-bullseye/
import time
import board
import busio
import digitalio
import socket

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess

from datetime import datetime, timedelta
import pytz
import re

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
hostname = socket.gethostname()

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Display Refresh
LOOPTIME = 0.001666

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

font = ImageFont.truetype('PixelOperator.ttf', 16)
#font = ImageFont.load_default()

while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

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
    cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
    Temp = subprocess.check_output(cmd, shell = True) 
    timecode = get_timecode_milliseconds()
    
    # Pi Stats Display
    draw.text((0, 0), "IP: " + str(IP,'utf-8'), font=font, fill=255)
    draw.text((0, 16), (f'Name: {Hostname}'), font=font, fill=255)

    draw.text((0, 32), str(CPU,'utf-8') + "LA", font=font, fill=255)
    draw.text((80, 32), str(Temp,'utf-8') , font=font, fill=255)

    # draw.text((0, 32), str(MemUsage,'utf-8'), font=font, fill=255)
    #draw.text((0, 48), str(Disk,'utf-8'), font=font, fill=255)

    draw.text((0, 48),f'TC: {timecode}', font=font, fill=255)
        
    # Display image
    oled.image(image)
    oled.show()
    time.sleep(LOOPTIME)
