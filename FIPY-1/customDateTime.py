
import time
import machine
from machine import RTC

rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
while not rtc.synced():
    machine.idle()
print("RTC synced with NTP time")
#adjust your local timezone, by default, NTP time will be GMT
time.timezone(8*60**2) 
x = time.localtime()


datetimeFormat = "[" + str(x[2]) + "/" + str(x[1]) + "/" + str(x[0]) + " | " + str(x[3]) + ":" + str(x[4]) + "]"

def customDateTime():
    return datetimeFormat

