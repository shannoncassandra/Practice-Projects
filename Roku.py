#Launches the Hulu app on the Roku.

from roku import Roku
import time

roku = Roku('192.168.0.207')

roku.home()
Hulu = roku['Hulu']
Hulu.launch()

#roku.play() = to play and pause
