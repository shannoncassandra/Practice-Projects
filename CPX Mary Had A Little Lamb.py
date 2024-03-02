#This code is for the Adafruit Circuit Playground. It will play the tune "Mary Had A Little Lamb" and flash colors to reveal the image of a lamb.

from adafruit_circuitplayground.express import cpx

import time

cpx.pixels.brightness = .01

# Tones
# cpx.play_tone(275, 1) C
# cpx.play_tone(294, 1) D
# cpx.play_tone(330, 1) E
# cpx.play_tone(349, 1) F
# cpx.play_tone(440, 1) G
# cpx.play_tone(494, 1) A
# cpx.play_tone(523, 1) B
 
cpx.pixels[3] = (255, 0, 0)
cpx.pixels[6] = (255, 0, 0)
cpx.play_tone(275, .25)
cpx.pixels[3] = (0, 0, 0)
cpx.pixels[6] = (0, 0, 0)

cpx.pixels[2] = (0, 255, 0)
cpx.pixels[7] = (0, 255, 0)
cpx.play_tone(250, .25)
cpx.pixels[2] = (0, 0, 0)
cpx.pixels[7] = (0, 0, 0)

cpx.pixels[1] = (255, 255, 0)
cpx.pixels[8] = (255, 255, 0)
cpx.play_tone(219, .25)
cpx.pixels[1] = (0, 0, 0)
cpx.pixels[8] = (0, 0, 0)

cpx.pixels[2] = (0, 255, 0)
cpx.pixels[7] = (0, 255, 0)
cpx.play_tone(250, .25)
cpx.pixels[2] = (0, 0, 0)
cpx.pixels[7] = (0, 0, 0)

cpx.pixels[9] = (255, 0, 255)
cpx.play_tone(275, .25) 
cpx.pixels[9] = (0, 0, 0)

cpx.pixels[9] = (255, 0, 255)
cpx.play_tone(275, .25) 
cpx.pixels[9] = (0, 0, 0)

cpx.pixels[0] = (255, 255, 255)
cpx.pixels[1] = (255, 255, 255)
cpx.pixels[2] = (255, 255, 255)
cpx.pixels[3] = (0, 0, 255)
cpx.pixels[4] = (255, 255, 255)
cpx.pixels[5] = (255, 255, 255)
cpx.pixels[6] = (0, 0, 255)
cpx.pixels[7] = (255, 255, 255)
cpx.pixels[8] = (255, 255, 255)
cpx.pixels[9] = (255, 255, 255)
cpx.play_tone(275, 1) 
cpx.pixels[0] = (0, 0, 0)
cpx.pixels[1] = (0, 0, 0)
cpx.pixels[2] = (0, 0, 0)
cpx.pixels[3] = (0, 0, 0)
cpx.pixels[4] = (0, 0, 0)
cpx.pixels[5] = (0, 0, 0)
cpx.pixels[6] = (0, 0, 0)
cpx.pixels[7] = (0, 0, 0)
cpx.pixels[8] = (0, 0, 0)
cpx.pixels[9] = (0, 0, 0)

cpx.pixels[0] = (255, 0, 255)
cpx.play_tone(250, .25)
cpx.pixels[0] = (0, 0, 0)

cpx.pixels[0] = (255, 0, 255)
cpx.play_tone(250, .25)
cpx.pixels[0] = (0, 0, 0)

cpx.pixels[0] = (255, 255, 255)
cpx.pixels[1] = (255, 255, 255)
cpx.pixels[2] = (255, 255, 255)
cpx.pixels[3] = (0, 0, 255)
cpx.pixels[4] = (255, 255, 255)
cpx.pixels[5] = (255, 255, 255)
cpx.pixels[6] = (0, 0, 255)
cpx.pixels[7] = (255, 255, 255)
cpx.pixels[8] = (255, 255, 255)
cpx.pixels[9] = (255, 255, 255)
cpx.play_tone(250, 1)
cpx.pixels[0] = (0, 0, 0)
cpx.pixels[1] = (0, 0, 0)
cpx.pixels[2] = (0, 0, 0)
cpx.pixels[3] = (0, 0, 0)
cpx.pixels[4] = (0, 0, 0)
cpx.pixels[5] = (0, 0, 0)
cpx.pixels[6] = (0, 0, 0)
cpx.pixels[7] = (0, 0, 0)
cpx.pixels[8] = (0, 0, 0)
cpx.pixels[9] = (0, 0, 0)

cpx.pixels[0] = (255, 0, 255)
cpx.pixels[9] = (255, 0, 255)
cpx.play_tone(275, .25) 
cpx.pixels[0] = (0, 0, 0)
cpx.pixels[9] = (0, 0, 0)

cpx.pixels[0] = (255, 255, 255)
cpx.pixels[1] = (255, 255, 255)
cpx.pixels[2] = (255, 255, 255)
cpx.pixels[3] = (0, 0, 255)
cpx.pixels[4] = (255, 255, 255)
cpx.pixels[5] = (255, 255, 255)
cpx.pixels[6] = (0, 0, 255)
cpx.pixels[7] = (255, 255, 255)
cpx.pixels[8] = (255, 255, 255)
cpx.pixels[9] = (255, 255, 255)
cpx.play_tone(330, .25)
cpx.pixels[0] = (0, 0, 0)
cpx.pixels[1] = (0, 0, 0)
cpx.pixels[2] = (0, 0, 0)
cpx.pixels[3] = (0, 0, 0)
cpx.pixels[4] = (0, 0, 0)
cpx.pixels[5] = (0, 0, 0)
cpx.pixels[6] = (0, 0, 0)
cpx.pixels[7] = (0, 0, 0)
cpx.pixels[8] = (0, 0, 0)
cpx.pixels[9] = (0, 0, 0)

cpx.pixels[0] = (255, 255, 255)
cpx.pixels[1] = (255, 255, 255)
cpx.pixels[2] = (255, 255, 255)
cpx.pixels[3] = (0, 0, 255)
cpx.pixels[4] = (255, 255, 255)
cpx.pixels[5] = (255, 255, 255)
cpx.pixels[6] = (0, 0, 255)
cpx.pixels[7] = (255, 255, 255)
cpx.pixels[8] = (255, 255, 255)
cpx.pixels[9] = (255, 255, 255)
cpx.play_tone(330, 1)
cpx.pixels[0] = (0, 0, 0)
cpx.pixels[1] = (0, 0, 0)
cpx.pixels[2] = (0, 0, 0)
cpx.pixels[3] = (0, 0, 0)
cpx.pixels[4] = (0, 0, 0)
cpx.pixels[5] = (0, 0, 0)
cpx.pixels[6] = (0, 0, 0)
cpx.pixels[7] = (0, 0, 0)
cpx.pixels[8] = (0, 0, 0)
cpx.pixels[9] = (0, 0, 0)
