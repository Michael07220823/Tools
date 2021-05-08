from hashlib import md5, sha256, sha384, sha512

def hash_string_md5(string = None):
    hash_str = md5(string.encode('utf-8')).hexdigest()
    return hash_str

def hash_string_sha256(string = None):
    hash_str = sha256(string.encode('utf-8')).hexdigest()
    return hash_str

def hash_string_sha384(string = None):
    hash_str = sha384(string.encode('utf-8')).hexdigest()
    return hash_str

def hash_string_sha512(string = None):
    hash_str = sha512(string.encode('utf-8')).hexdigest()
    return hash_str


def read_file(file_path = None):
    with open(file_path, 'rb') as f:
        file_content = f.read()
    return file_content

def hash_file_md5(file_path = None):
    data = read_file(file_path)
    hash_code = md5(data).hexdigest()
    return hash_code

def hash_file_sha256(file_path = None):
    data = read_file(file_path)
    hash_code = sha256(data).hexdigest()
    return hash_code

def hash_file_sha384(file_path = None):
    data = read_file(file_path)
    hash_code = sha384(data).hexdigest()
    return hash_code

def hash_file_sha512(file_path = None):
    data = read_file(file_path)
    hash_code = sha512(data).hexdigest()
    return hash_code