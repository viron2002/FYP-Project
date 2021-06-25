import time
import pycom
import machine
from customDateTime import customDateTime
from pycoproc_2 import Pycoproc
from SI7006A20 import SI7006A20
from MPL3115A2 import MPL3115A2

py = Pycoproc()
et = SI7006A20(py)
st = MPL3115A2(py)


pybytes.send_signal(1, str(customDateTime()) + " Sensor Temperature: " + str(st.temperature()))
time.sleep(2)
pybytes.send_signal(1, str(customDateTime()) + " External Temperature: " + str(et.temperature()))
time.sleep(2)
pybytes.send_signal(1, str(customDateTime()) + " Humidity: " + str(et.humidity()))
time.sleep(10)