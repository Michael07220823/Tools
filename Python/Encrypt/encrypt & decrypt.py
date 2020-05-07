def encrypt_key_generate(num_key = int()):
    from cryptography.fernet import Fernet

    if num_key != int():
        print("\n[INFO] Random generate key:")
        for i in range(1, num_key + 1):
            key = Fernet.generate_key().decode('utf-8')
            print(str(i) + '. ' + key)
    else:
        key = Fernet.generate_key().decode('utf-8')
        print("\n[INFO] Random generate key: \n", key)
    return key

    
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
    print("\n[INFO] decrypt message output: \n", decry_message.decode("utf8"))
    return decrypt_message
    



if __name__ == "__main__":
    try:
        while True:
            print("\n[INFO] 1. is encrypt, 2. is decrypt")
            choice = input("[INFO] Please input numeric: ")
            count = int(input("[INFO] Please input execute count: "))
            if int(choice) == 1:
                key = encrypt_key_generate()
                for i in range(count):
                    word = input("[INFO] Please input message of encrypt:\n")
                    encrypt_content = encrypt_message(key=key, message=word)
            else:
                key = input("[INFO] Please input key: ")
                for i in range(count):
                    encrypt_message = input("[INFO] Please input encrypt message:\n")
                    decrypt_message(key=key, message=encrypt_message)
    except KeyboardInterrupt:
        print("\n[INFO] Program be interrupt !")
    except Exception as error:
        print("[INFO] Exception: %s" % str(error))
    finally:
        import os
        os.system("pause")

# Reference: https://riptutorial.com/zh-TW/python/example/27070/%E7%B7%A8%E7%A2%BC%E5%92%8C%E8%A7%A3%E7%A2%BCbase64
# Reference: https://nitratine.net/blog/post/encryption-and-decryption-in-python/#encrypting