import psutil

# print(psutil.net_io_counters())

# for pid in psutil.net_connections(kind="tcp4"):
#     print(pid)

# print(psutil.net_if_addrs())
print(psutil.net_if_stats())