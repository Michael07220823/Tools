def encrypt_file(key = None, encrypt_file_path = str(), output_file_path = str()):
    from cryptography.fernet import Fernet
    import os

    if key == None:
        key = Fernet.generate_key().decode('utf-8')
        fernet_key = Fernet(key)
    print("[INFO] Please save key:", key)

    with open(encrypt_file_path + '.encrypt_key', 'w') as f:
        f.write(key)

    with open(encrypt_file_path, 'rb') as f:
        content = f.read()
        encrypt_content = fernet_key.encrypt(content)
    
    if output_file_path != str():
        path = output_file_path + os.path.split(encrypt_file_path)[1] + '.encrypt_file' + os.path.splitext(encrypt_file_path)[1]
        with open(path, 'wb') as f2:
            f2.write(encrypt_content)
    else:
        path = encrypt_file_path + '.encrypt_file' + os.path.splitext(encrypt_file_path)[1]
        with open(path, 'wb') as f2:
            f2.write(encrypt_content)

    return path


def decrypt_file(key = None, encrypt_file_path = str(), output_file_path = str()):
    from cryptography.fernet import Fernet
    import os

    if key == None:
        print("[INFO] Didn't give encrypt key !")
    else:
        fernet_key = Fernet(key)

    with open(encrypt_file_path, 'rb') as f:
        content = f.read()
        decrypt_content = fernet_key.decrypt(content)
        
        path = output_file_path + os.path.split(encrypt_file_path)[1] + '.decrypt_file' + os.path.splitext(encrypt_file_path)[1]
        with open(path, 'wb') as f2:
            f2.write(decrypt_content)

        return path

# Reference: https://nitratine.net/blog/post/encryption-and-decryption-in-python/
# Reference: http://ijecorp.blogspot.com/2013/08/python-m2crypto-aes-encrypt-decrypt.html