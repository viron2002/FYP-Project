from pycoproc_2 import Pycoproc
from SI7006A20 import SI7006A20
from MPL3115A2 import MPL3115A2
from customDateTime import customDateTime
import time


py = Pycoproc()
lt = SI7006A20(py)
lp = MPL3115A2(py)



pybytes.send_signal(2, str(customDateTime()) + ": " + "Sensor Temperature: " + str(lp.temperature()))
time.sleep(3)
pybytes.send_signal(2, str(customDateTime()) + ": " + "External Temperature: " + str(lt.temperature()))
