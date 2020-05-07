def encrypt_message(key = str(), message = str()):
    from cryptography.fernet import Fernet

    # Encode str to bytes.
    key = bytes(key, encoding="utf8")
    message = bytes(message, encoding="utf8")

    # Encrypt key, must has 32 bit length.
    fernet_key = Fernet(key)
    
    encrypt_content = fernet_key.encrypt(message)
    print("[INFO] Encrypt message output: \n", encrypt_content.decode())
    return encrypt_content


def decrypt_message(key = str(), message = str()):
    from cryptography.fernet import Fernet

    # Encode str to bytes.
    key = bytes(key, encoding="utf8")
    message = bytes(message, encoding="utf8")

    fernet_key = Fernet(key)
    decry_message = fernet_key.decrypt(message)
    print("[INFO] decrypt message output: \n", decry_message.decode("utf8"))
    return decrypt_message
    

def encrypt_key_generate(num_key = int()):
    from cryptography.fernet import Fernet

    if num_key != int():
        print("[INFO] Random generate key:")
        for i in range(1, num_key + 1):
            key = Fernet.generate_key().decode('utf-8')
            print(str(i) + '. ' + key)
    else:
        key = Fernet.generate_key().decode('utf-8')
        print("[INFO] Random generate key: \n", key)
    return key

# Reference: https://riptutorial.com/zh-TW/python/example/27070/%E7%B7%A8%E7%A2%BC%E5%92%8C%E8%A7%A3%E7%A2%BCbase64
# Reference: https://nitratine.net/blog/post/encryption-and-decryption-in-python/#encrypting