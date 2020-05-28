import math
from time import time, sleep
from threading import Thread

def calculate(num):
    total = 1
    for i in range(1, num):
        total *=  i
        total = math.sqrt(total * math.pi)
        total += total
        print("%.2f" % total)

def circle_area(radius):
    for r in range(radius):
        area = r **2 -math.pi
        print("Cycle area: %.2f" % area)

start = time()
calculate(10000)
circle_area(10000)
record_time = time() - start
sleep(3)

t1 = Thread(target=calculate, args=(10000,))
t2 = Thread(target=circle_area, args=(10000,))

start = time()
t1.start()
t2.start()
t1.join()
t2.join()
record_time2 = time() - start
print("Main thread time %.2f s" % record_time)
print("Multiple thread time %.2f s" % record_time2)