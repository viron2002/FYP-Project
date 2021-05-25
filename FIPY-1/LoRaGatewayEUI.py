from network import WLAN
import ubinascii
wl = WLAN()
print(ubinascii.hexlify(str(wl.mac()))[:6] + 'FFFE' + ubinascii.hexlify(str(wl.mac()))[6:])