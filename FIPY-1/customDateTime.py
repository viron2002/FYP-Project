import time
import machine
from machine import RTC

def datetime():    

    rtc = machine.RTC()
    rtc.ntp_sync("pool.ntp.org")

    #adjust your local timezone, by default, NTP time will be GMT
    time.timezone(8*60**2) 
    x = time.localtime()


    datetimeFormat = " [ " + str(x[2]) + "/" + str(x[1]) + "/" + str(x[0]) + " | " + str(x[3]) + ":" + str(x[4]) + " ] "


    return datetimeFormat

