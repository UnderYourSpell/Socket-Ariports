import socket
import threading

SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


class Client:


    def __init__(self,sock=None,tier = int, name = str):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.tier = tier
            self.name = name
            self.host = ''
            self.port = 5050
            self.dest = "ZZZ"
            self.payload = ""
            self.type = "c"
        
    def connect(self,host,port):
        server_address = (host,port)
        self.host = host
        self.port  = port
        self.sock.connect(server_address)
        print(f"[CONNECTED] Client connected to server at {host}:{port}")

    def update_info(self,dest,payload):
        self.dest = dest
        self.payload = payload

    def dest(self):
        return self.dest

    def run(self):
        connected = True
        dest  = self.dest
        payload = self.payload
        #delimiter = '\n'
        message = self.type + '\n' + self.name + '\n' + dest + '\n' + payload + '\n'

        self.sock.send(message.encode(FORMAT))
        #self.sock.send(self.payload.encode(FORMAT))

        
        self.sock.close()
