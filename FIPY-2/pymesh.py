import time

if pybytes is not None:
    if pybytes.__pymesh and pybytes.__pymesh.__pymesh:
        pymesh = pybytes.__pymesh.__pymesh
        while True:
            pkt = "Hello, from " + str(pymesh.mac())
            pybytes.send_signal(1, pkt)
            time.sleep(20)

print("Hello World")