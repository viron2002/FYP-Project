
def wifiAP(ap): 
    from network import WLAN
    wlan = WLAN()

    if ap == True:
        #Password 8 letters
        wlan.init(mode=WLAN.AP, ssid="FIPY1", auth=(WLAN.WPA2, "1a2b3c4d"))
        wlan.ifconfig(id=1)
        print("AP Mode\n") #id=1 signifies the AP interface

    elif ap == False:
        wlan.ifconfig(id=0)
        print("Station Mode\n")

    else:
        print("Invalid")

