from SI7006A20 import SI7006A20
import math
class abc :
    def connection_status():
        if pybytes.isconnected():
            print("Connected")
        else :
            pybytes.connect()
            print("Connecting now")

    def display():
        # from SI7006A20 import SI7006A20
        obj = SI7006A20()
        print("The humidity in % is in pybytes ")
        value1 = obj.humidity()
        pybytes.send_signal(3, math.ceil(value1))
        print("")
        print("Temperature in degree is pybytes ")
        value2 = obj.temperature()
        pybytes.send_signal(4, math.ceil(value2))
