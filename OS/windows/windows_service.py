import psutil

for item in psutil.win_service_iter():
    print(item)