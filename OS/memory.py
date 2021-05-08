import os
import time
import psutil

info = psutil.virtual_memory()

print ('總記憶體：', info.total)
print ('記憶體目前使用：', psutil.Process(os.getpid()).memory_info().rss)
print ('記憶體目前使用率：', info.percent)
print ('交換記憶體目前使用率：', psutil.swap_memory())