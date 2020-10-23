# -*- coding: utf-8 -*-
import json
import socket

# HOST & PORT
HOST = "127.0.0.1"
# HOST = socket.gethostname()
PORT = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)
server.settimeout(120)

print("[INFO] Starting listen on {} {} port...".format(HOST, PORT))
conn, addr = server.accept()

print("[INFO] Connect IP: {}".format(str(addr[0]) + ':' + str(addr[1])))


while True:
    client_message = conn.recv(4096).decode("utf-8")
    print('[INFO] Client message is:', client_message)

    server_message = "Received !"
    conn.sendall(server_message.encode())
    

    if client_message == 'q':
        print('[INFO] Stop server !')
        conn.close()
        break
    # 超過30秒沒有接收到訊息，即中斷連線
    conn.settimeout(30)