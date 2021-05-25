from pycoproc_2 import Pycoproc

from MPL3115A2 import MPL3115A2

import time


py = Pycoproc()

lp = MPL3115A2(py)

i = 0
while i = 0:
    pybytes.send_signal(2, lp.temperature())
    time.sleep(10)