# Usage
# python euclidean_algorithm.py -f 1920 -s 1080

import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--fir_num", required = True, help = "First number.")
ap.add_argument("-s", "--sec_num", required = True, help = "Second number.")
args = vars(ap.parse_args())

first = int(args["fir_num"])
second = int(args["sec_num"])
a = first
b = second

while b != 0:
    temp = a % b
    a = b
    b = temp

print("Num: %d:%d" % (first/a*30, second/a*30 ))