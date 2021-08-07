import pycom
import time
import machine
from network import WLAN

wlan = WLAN()



def wifiConnect(ssidn, pw):
    wlan.init(mode=WLAN.STA)
    wlan.connect(ssid=ssidn, auth=(WLAN.WPA2, pw), timeout=20000)
    print("Connecting to " + ssidn + " with 20 seconds timeout\n")
    pycom.heartbeat(False)
    pycom.rgbled(0xff6000)
    time.sleep(10)
    pycom.rgbled(0)


    if wlan.isconnected() == True:
        pycom.rgbled(0x007f00)
        print("Connected to WiFi: " + ssidn)
        time.sleep(10)
        pycom.heartbeat(True)
        
    
    else:
        pycom.rgbled(0xff0000)
        print("Fail to connect to WiFi")
        time.sleep(10)
        pycom.heartbeat(True)



def wifiAP(ap):

    if ap == True:
        #Password 8 letters
        wlan.init(mode=WLAN.AP, ssid="FIPY1", auth=(WLAN.WPA2, "1a2b3c4d")) #eightletters
        print("Access Point mode, ssid = FIPY1, password = 1a2b3c4d\n")
        pycom.heartbeat(False)
        pycom.rgbled(0x00ff)


    elif ap == False:
        wlan.init(mode=WLAN.STA)
        print("Station Mode\n")
        pycom.heartbeat(True)



def wifiScan():

    print("Scanning and Displaying nearby WiFi")

    wlan = WLAN(mode=WLAN.STA)

    scan = wlan.scan()

    wifiname = []
    i = 1
    for s in scan:
        print(str(i) + ". " + s.ssid)
        wifiname.append(s.ssid)
        i += 1
        

"""def wifiAntenna():

    wlan.antenna(WLAN.EXT_ANT)"""