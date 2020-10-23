import socket

# Host and Port
HOST = "127.0.0.1"
# HOST = socket.gethostname()
PORT = 80


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
status = client.connect_ex((HOST, PORT))
# print(status)

while True:
    client_message = input("[INFO] Input message:")
    client.sendall(client_message.encode("utf-8"))

    server_message = client.recv(4096).decode("utf-8")
    print('[INFO] Server message:', server_message)

    if client_message == 'q':
        print("[INFO] Stop connect !")
        client .close()
        break
