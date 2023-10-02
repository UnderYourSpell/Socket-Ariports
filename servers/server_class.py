import socket


class Server():

    def __init__(self,sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.server_address = ('',0000)

    def bind(self,host,port):
        self.server_address = (host,port)
        self.sock.bind(self.server_address)  

    def run(self):
        pass