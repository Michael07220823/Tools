import os

def get_file_size(path=str()):
    # Return size unit is byte, so need to transfer to kilo byte.
    size = round(os.path.getsize(path) / 1024, 2)
    print("[INFO] File size: %.2f Kbytes" % size)
    return size