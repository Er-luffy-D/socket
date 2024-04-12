import socket

HEADER=64
PORT=5050
FORMAT="utf-8"
DISCONNECTED_MSG="!bye"
SERVER="192.168.70.103"
ADDR=(SERVER,PORT)
msg=""
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b''*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

while msg!=DISCONNECTED_MSG:
    msg=input("ENTER YOUR MESSAGE: ")
    send(msg)