# Created by: Michael Klements
# For Raspberry Pi Desktop Case with OLED Stats Display
# Base on Adafruit CircuitPython & SSD1306 Libraries
# Installation & Setup Instructions - https://www.the-diy-life.com/add-an-oled-stats-display-to-raspberry-pi-os-bullseye/
import time
import board
import busio
import digitalio
import time

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess
import time

from datetime import datetime, timedelta
import re

def get_timecode_milliseconds():
  # current time in seconds
  sec = datetime.now().timestamp()
  #print('Time in seconds:', sec)

  # convert to Days, hh:mm:ss
  td = str(timedelta(seconds=sec))
  #print(td)
  td = re.search(r",(.*)", td) 
  return str(td.group(1))


def x_get_timecode_milliseconds():
  """Gets the timecode in milliseconds in Linux using Python.

  Returns:
    A string representing the timecode in milliseconds in the format HH:MM:SS.XXX.
  """

  # Get the current time in seconds since the epoch.
  seconds_since_epoch = time.time()

  # Convert the seconds since the epoch to milliseconds.
  milliseconds_since_epoch = seconds_since_epoch * 1000

  # Get the timecode in HH:MM:SS format.
  timecode_hhmmss = time.strftime("%H:%M:%S", time.gmtime(seconds_since_epoch))

  # Split the timecode into hours, minutes, and seconds.
  hours, minutes, seconds = timecode_hhmmss.split(":")

  # Convert the seconds to milliseconds.
  milliseconds = int(seconds) * 1000

  # Add the milliseconds to the timecode in HH:MM:SS format.
  timecode_milliseconds = "%s.%03d" % (timecode_hhmmss, milliseconds)

  return str(timecode_milliseconds)

# Get the timecode in milliseconds.
timecode_milliseconds = get_timecode_milliseconds()

# Print the timecode in milliseconds.
print(timecode_milliseconds)

def old_get_timecode_milliseconds():
  """Get the current time in milliseconds."""
  return str(int(time.perf_counter_ns() / 1000000))

print(get_timecode_milliseconds())

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Parameters
WIDTH = 128
HEIGHT = 32
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
    MemUsage = subprocess.check_output(cmd, shell = True )
    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell = True )
    cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
    Temp = subprocess.check_output(cmd, shell = True) 
    timecode = get_timecode_milliseconds()
    
    # Pi Stats Display
    #draw.text((0, 0), "IP: " + str(IP,'utf-8'), font=font, fill=255)
    #draw.text((0, 16), str(CPU,'utf-8') + "LA", font=font, fill=255)
    #draw.text((80, 16), str(Temp,'utf-8') , font=font, fill=255)
    #draw.text((0, 32), str(MemUsage,'utf-8'), font=font, fill=255)
    #draw.text((0, 48), str(Disk,'utf-8'), font=font, fill=255)
    draw.text((0, 0),timecode, font=font, fill=255)
        
    # Display image
    oled.image(image)
    oled.show()
    time.sleep(LOOPTIME)
