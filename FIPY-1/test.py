x = "test\ntest"
a = x.decode('utf-8')
pybytes.send_signal(2, a)