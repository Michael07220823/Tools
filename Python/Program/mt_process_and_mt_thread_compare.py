import math
from time import time
import multiprocessing as mp
from threading import Thread as Td
from memory_profiler import profile


@profile
def calculate(num):
    total = 1
    for i in range(1, num):
        total *=  i
        total = math.sqrt(total * math.pi)
        total += total
        print("%.2f" % total)


@profile
def circle_area(radius):
    for r in range(radius):
        area = r **2 -math.pi
        print("Cycle area: %.2f" % area)


if __name__ == "__main__":
    # Main processing.
    start = time()
    calculate(1000)
    circle_area(1000)
    end1 = time()-start


    # Multiple thread.
    start = time()
    t1 = Td(target=calculate, args=(1000,))
    t1.name = "t1-calculate"
    t2 = Td(target=circle_area, args=(1000,))
    t2.name = "t2-circle_area"

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    end2 = time()-start


    # Multiple processing.
    start = time()
    p1 = mp.Process(target=calculate, args=(1000,))
    p2 = mp.Process(target=circle_area, args=(1000,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end3 = time()-start

    # Compare costing time.
    print("Main processing cost time %.2fs" % end1)
    print("Multiple thread cost time %.2fs" % end2)
    print("Multiple processing cost time %.2fs" % end3)