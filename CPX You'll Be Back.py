#This code is for the Adafruit Circuit Playground. It will play the tune "You'll Be Back" from the muscial Hamilton and flash various colors in sync with the tune.

# go to https://www.youtube.com/watch?v=eKFN-aqPJH8
# set it at 0:41 and pause
# run code and then hit play on video

from adafruit_circuitplayground.express import cpx  # imports the CPX library from its subfolder

import time

cpx.pixels.brightness = .01                     # set pixel brightness
cpx.pixels.fill((0, 0, 0))                          # turns all pixels off
cpx.pixels.show()                                   # sends data to pixels

time.sleep(0.5)

for i in range(1):
#you'll be back
	cpx.pixels[2] = (255, 0, 0)
	time.sleep(0.45)
	cpx.pixels[2] = (0, 0, 0)
	cpx.pixels[1] = (0, 255, 0)
	time.sleep(0.45)
	cpx.pixels[1] = (0, 0, 0)
	cpx.pixels[0] = (0, 0, 255)
	time.sleep(1)
	cpx.pixels[0] = (0, 0, 0)
#wait and see
	cpx.pixels[2] = (255, 0, 0)
	time.sleep(0.45)
	cpx.pixels[2] = (0, 0, 0)
	cpx.pixels[1] = (0, 255, 0)
	time.sleep(0.45)
	cpx.pixels[1] = (0, 0, 0)
	cpx.pixels[0] = (0, 0, 255)
	time.sleep(1)
	cpx.pixels[0] = (0, 0, 0)
#you re
	cpx.pixels[2] = (255, 0, 0)
	time.sleep(0.35)
	cpx.pixels[2] = (0, 0, 0)
	cpx.pixels[1] = (0, 255, 0)
	time.sleep(0.5)
	cpx.pixels[1] = (0, 0, 0)
#member you belong to
	cpx.pixels[4] = (255, 0, 255)
	time.sleep(0.35)
	cpx.pixels[4] = (0, 0, 0)
	cpx.pixels[3] = (0, 255, 255)
	time.sleep(0.1)
	cpx.pixels[3] = (0, 0, 0)
	cpx.pixels[4] = (255, 0, 255)
	time.sleep(0.35)
	cpx.pixels[4] = (0, 0, 0)
	cpx.pixels[3] = (0, 255, 255)
	time.sleep(0.1)
	cpx.pixels[3] = (0, 0, 0)
	cpx.pixels[4] = (255, 0, 255)
	time.sleep(0.6)
	cpx.pixels[4] = (0, 0, 0)
	cpx.pixels[3] = (0, 255, 255)
	time.sleep(0.2)
	cpx.pixels[3] = (0, 0, 0)
#me
	cpx.pixels[2] = (255, 0, 0)
	time.sleep(1)
	cpx.pixels[2] = (0, 0, 0)
  
  
  
  # OR control with a button start
  
from adafruit_circuitplayground.express import cpx  # imports the CPX library from its subfolder

import time

cpx.pixels.brightness = .01                     # set pixel brightness
cpx.pixels.fill((0, 0, 0))                          # turns all pixels off
cpx.pixels.show()                                   # sends data to pixels

while True:                         
    if cpx.button_b:
#you'll be back
        cpx.pixels[2] = (255, 0, 0)
        time.sleep(0.45)
        cpx.pixels[2] = (0, 0, 0)
        cpx.pixels[1] = (0, 255, 0)
        time.sleep(0.45)
        cpx.pixels[1] = (0, 0, 0)
        cpx.pixels[0] = (0, 0, 255)
        time.sleep(1)
        cpx.pixels[0] = (0, 0, 0)
#wait and see
        cpx.pixels[2] = (255, 0, 0)
        time.sleep(0.45)
        cpx.pixels[2] = (0, 0, 0)
        cpx.pixels[1] = (0, 255, 0)
        time.sleep(0.45)
        cpx.pixels[1] = (0, 0, 0)
        cpx.pixels[0] = (0, 0, 255)
        time.sleep(1)
        cpx.pixels[0] = (0, 0, 0)
#you re
        cpx.pixels[2] = (255, 0, 0)
        time.sleep(0.35)
        cpx.pixels[2] = (0, 0, 0)
        cpx.pixels[1] = (0, 255, 0)
        time.sleep(0.5)
        cpx.pixels[1] = (0, 0, 0)
#member you belong to
        cpx.pixels[4] = (255, 0, 255)
        time.sleep(0.35)
        cpx.pixels[4] = (0, 0, 0)
        cpx.pixels[3] = (0, 255, 255)
        time.sleep(0.1)
        cpx.pixels[3] = (0, 0, 0)
        cpx.pixels[4] = (255, 0, 255)
        time.sleep(0.35)
        cpx.pixels[4] = (0, 0, 0)
        cpx.pixels[3] = (0, 255, 255)
        time.sleep(0.1)
        cpx.pixels[3] = (0, 0, 0)
        cpx.pixels[4] = (255, 0, 255)
        time.sleep(0.6)
        cpx.pixels[4] = (0, 0, 0)
        cpx.pixels[3] = (0, 255, 255)
        time.sleep(0.2)
        cpx.pixels[3] = (0, 0, 0)
#me
        cpx.pixels[2] = (255, 0, 0)
        time.sleep(1)
        cpx.pixels[2] = (0, 0, 0)
