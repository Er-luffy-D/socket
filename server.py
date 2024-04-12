import socket
import threading

# CONSTANT VALUES
HEADER=64   # Used for defining msg lenght.

PORT =5050

# SERVER="192.168.70.103"
SERVER=socket.gethostbyname(socket.gethostname())
# print(socket.gethostname())     # this return LAPTOP-DJOA3TR (host name) name which represents your computer on network
# print(SERVER)     # this return IPV4 address

ADDR=(SERVER,PORT)
DISCONNECTED_MSG="!bye"
FORMAT="utf-8"

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def geTCLIENT(conn,addr):
    print(f"[NEW CONNECTION]: {addr} connected.")
    Connected=True
    while Connected:
        msg_Lenght=conn.recv(HEADER).decode(FORMAT)
        if msg_Lenght:
            msg_Lenght=int(msg_Lenght)
            msg=conn.recv(msg_Lenght).decode(FORMAT)
            if msg==DISCONNECTED_MSG:
                Connected=False
            print(f"[{addr}] : {msg}")
            conn.send(f"MSG RECIEVED FROM {addr}".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] server is listening at {SERVER}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=geTCLIENT,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")

print("[STARTING] server is starting ...")
start()