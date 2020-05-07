import os
import time
import psutil

info = psutil.virtual_memory()

print ('cpu個數：', psutil.cpu_count(logical=False))
for i in psutil.cpu_times(percpu=True):
    print(i)
print ('cpu使用率：', psutil.cpu_percent(interval=1, percpu=True))
print ('cpu頻率：', psutil.cpu_freq(percpu=True))