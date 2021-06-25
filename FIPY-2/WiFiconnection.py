from network import WLAN
import machine
wlan = WLAN(mode=WLAN.STA)

x = 1
wlan.connect(ssid='ssid', auth=(WLAN.WPA2, 'password'))
for x in range(3):

    if not wlan.isconnected():
        ("WiFi not connected... Trying again (" + i + ")")
        ++i

    else:
        break


print("WiFi connected succesfully")
print(wlan.ifconfig())