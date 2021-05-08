import psutil
import datetime

# print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
# print(psutil.users())
# print(psutil.pids())

for proc in psutil.process_iter(['pid', 'name', 'username', 'exe', 'status', 'uids', 'gids'
                                'cpu_percent', 'memory_info', 'num_threads', 'cpu_affinity', 'memory_percent']):
    print(proc.info)