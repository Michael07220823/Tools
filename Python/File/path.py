# 適用Linux and Windows
import os

def get_file_name(path = None):
    return os.path.basename(path)

def get_abs_file_name(path = None):
    return os.path.abspath(path)

def get_diretory_name(path = None):
    return os.path.dirname(path)

def get_deputy_file_name(path = None):
    return os.path.splitext(path)[1]