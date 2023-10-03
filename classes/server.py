import socket
import threading

SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

class Server():

    def __init__(self,sock=None,tier = int,name  = str):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.server_address = ('',0000)
            self.tier = tier
            self.name  = name
            self.arrived = []
            self.host = ''
            self.port = 5050

    def bind(self,host,port):
        self.server_address = (host,port)
        self.host = host
        self.port = port
        self.sock.bind(self.server_address)

    def handle_client(self,conn,addr): #will handle multiple client connections at once
        print(f"NETWORK CONNECTION] {addr} connected.")

        connected  = True
        while connected:
            msg = conn.recv(SIZE).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False

            print(f"[{addr}] {msg}")
            msg = f"Msg received: {msg}"
            conn.send(msg.encode(FORMAT))
        conn.close()

    def run(self):
        print("Starting server")
        self.sock.listen()
        print(f"Listenting on {self.host}:{self.port}")


        while True:
            conn, addr = self.sock.accept()
            thread = threading.Thread(target = self.handle_client, args = (conn,addr))
            thread.start()
            print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')