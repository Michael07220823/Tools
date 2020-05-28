import math
from time import time, sleep
import multiprocessing as mp

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

if __name__ == '__main__':  #必須放這段代碼，不然會Error
    start = time()
    calculate(10000)
    circle_area(10000)
    end = time()-start
    sleep(3)

    ap = mp.Process(target=calculate, args=(10000,))
    jk = mp.Process(target=circle_area, args=(10000,))

    start = time()
    # 開始加速執行
    ap.start()
    jk.start()
    # 結束多進程
    ap.join()
    jk.join()
    end2 = time()-start

    print("Main processing cost time %.2fs" % end)
    print("Multiprocessing cost time %.2fs" % end2)