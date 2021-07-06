from network import WLAN
wlan = WLAN()


wlan.init(mode=WLAN.AP, ssid='FIPY1')

print(wlan.ifconfig(id=1)) #id =1 signifies the AP interface