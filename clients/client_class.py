import socket

class Client:

    def __init__(self,sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    def connect(self,host,port):
        server_address = (host, port)
        self.sock.connect(server_address)
    
