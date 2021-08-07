from pycoproc_2 import Pycoproc
from SI7006A20 import SI7006A20
from MPL3115A2 import MPL3115A2
from customDateTime import datetime
from _pybytes import Pybytes
from _pybytes_config import PybytesConfig
import time

conf = PybytesConfig().read_config()
pybytes = Pybytes(conf)

py = Pycoproc()
Etemp = SI7006A20(py)
Stemp = MPL3115A2(py)


def temp(run, MaxWarn, MinWarn):
    
    print("Getting Sensor Temperature and Room Temperature...")
    while run == True:
        
        
        #current_time = time.strtime("%H:%M:%S", t)
        
        if (Etemp.temperature() >= MaxWarn) == True: 
            print(datetime() + "Sensor Temperature: " + str(Stemp.temperature()))
            time.sleep(3)
            print(datetime() + "Room Temperature: " + str(Etemp.temperature()))
            time.sleep(3)
            print("\nWarning! Temperature exceeding " + str(MaxWarn) + " degrees Celcius\n")
            

            if pybytes.isconnected() == True:
                pybytes.send_signal(1, datetime() + "Sensor Temperature: " + str(Stemp.temperature()))
                pybytes.send_signal(2, datetime() + "Room Temperature: " + str(Etemp.temperature()))
                pybytes.send_signal(3,"Warning! Temperature exceeding " + str(MaxWarn) + "degrees Celcius")
                
            time.sleep(15)

        elif (Etemp.temperature() <= MinWarn) == True:
            print(datetime() + "Sensor Temperature: " + str(Stemp.temperature()))
            time.sleep(3)
            print(datetime() + "Room Temperature: " + str(Etemp.temperature()))
            time.sleep(3)
            print("\nWarning! Temperature dropping " + str(MinWarn) + " degrees Celcius\n")
            

            if pybytes.isconnected() == True:
                pybytes.send_signal(1, datetime() + "Sensor Temperature: " + str(Stemp.temperature()))
                pybytes.send_signal(2, datetime() + "Room Temperature: " + str(Etemp.temperature()))
                pybytes.send_signal(3,"Warning! Temperature dropping " + str(MinWarn) + "degrees Celcius")

        else:
            print(datetime() + "Sensor Temperature: " + str(Stemp.temperature()))
            time.sleep(3)
            print(datetime() + "Room Temperature: " + str(Etemp.temperature()))
            

            if pybytes.isconnected() == True:
                pybytes.send_signal(1, datetime() + "Sensor Temperature: " + str(Stemp.temperature()))
                pybytes.send_signal(2,datetime() + "Room Temperature: " + str(Etemp.temperature()))
                

            time.sleep(15)

            
            



"""def temp(run):

    while run == True:

        py = Pycoproc()
        lt = SI7006A20(py)
        lp = MPL3115A2(py)

        t = time.localtime()
        print("Getting Sensor Temperature and Room Temperature...")
        current_time = time.strtime("%H:%M:%S", t)
        
        print(current_time + "Sensor Temperature: " + str(lp.temperature()))
        print(current_time + "Room Temperature: " + str(lt.temperature()))
        time.sleep(15)"""

        
    
