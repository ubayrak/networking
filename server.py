import socket

host = '10.96.4.57'
port = 2323
FORMAT = 'utf-8'
EXIT = 'exit'
AD = (host, port)
list_of_clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket created with IPv4 and TCP features
s.bind(AD)


def rx(conn, addr):
    msg = conn.recv(1024).decode(FORMAT)
    print(f"[{addr}] : {msg}")
    return msg


def tx(conn):
    mesaj = input()
    conn.send(mesaj.encode(FORMAT))


#Program Starts
s.listen()
print(f"[LISTENING] Server is listening on {host}:{port}")
#Connection acceptance

while True:
    client, addr = s.accept()
    list_of_clients.append(client)
    print(f"[NEW CONNECTION] connected. {len(list_of_clients)}")
    # name = client.recv(1024).decode(FORMAT)
    # print(f"{name} is in")
"""
her biri ismini gondersin, sonra da thread ve broadcast calis..
"""

# connection = True
# while connection:
#     msg = rx(client, addr)
#     if msg == EXIT:
#         connection = False
    

# client.close()
