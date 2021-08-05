 
from network import WLAN
import machine
wlan = WLAN()


        #Password 8 letters
wlan.init(mode=WLAN.AP, ssid="FIPY2", auth=(WLAN.WPA2, "1a2b3c4d"))
wlan.ifconfig(id=1)
print("AP Mode\n")