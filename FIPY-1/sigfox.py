from network import Sigfox
import binascii
from SI7006A20 import SI7006A20
import socket
import pycom
import struct

from pycoproc_2 import Pycoproc

py = Pycoproc()
lt = SI7006A20(py)

# initalise Sigfox for RCZ1 (You may need a different RCZ Region) SG is RC4
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ4)

# print Sigfox Device ID
print(binascii.hexlify(sigfox.id()))

# print Sigfox PAC number
print(binascii.hexlify(sigfox.pac()))

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

# send data
# to sigfox 
s.send(str(SI7006A20().temperature()))
# to display 
print(str(SI7006A20().temperature()))

