from network import WLAN
import machine
import time

while not wlan.isconnected():
    print("WiFi not connected")
    time.sleep(60)