from network import WLAN

def wifiscan():
    wlan = WLAN(mode=WLAN.STA)

    scan = wlan.scan()

    wifiname = []
    i = 1
    for s in scan:
        print(str(i) + ") " + s.ssid)
        wifiname.append(s.ssid)
        i += 1
        
    return wifiname

print(wifiscan())

    
