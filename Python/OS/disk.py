import shutil

def sign_sort():
    print("%s" % ('-'*20))

def display_disk_usage_status(disk_path='C'):
    disk_path = disk_path.upper() + ':'
    sign_sort()
    print("|Disk : " + disk_path + ' '*10 + '|')
    sign_sort()

    disk_status = list()
    unit = "GB"

    # Original unit is bytes, and convert unit to GigaByte.
    space_usage = shutil.disk_usage(disk_path)
    for item in space_usage:
        disk_status.append(round(item/1024**3, 2))

    print("|Total:{:>9.2f} {} {}".format(disk_status[0], unit, '|'))
    print("|Used :{:>9.2f} {} {}".format(disk_status[1], unit, '|'))
    print("|Free :{:>9.2f} {} {}".format(disk_status[2], unit, '|'))
    sign_sort()

if __name__ == "__main__":
    import psutil

    display_disk_usage_status("F")
    print(psutil.disk_partitions(all=True))
    print(psutil.disk_usage("C:"))
    print(psutil.disk_io_counters(perdisk=True))