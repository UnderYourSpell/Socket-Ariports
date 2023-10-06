import socket
import threading

SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


class Client:


    def __init__(self,sock=None,name = str):
        if sock is None:
            self.name = name
            self.host = ''
            self.port = 5050
            self.dest = "ZZZ"
            self.payload = ""
            self.type = "c"
            self.allowed_airports = []
            self.cont = ''

    #def function to send message, already kind of written in run
    #def function to check if airport is allowed
    def init_allowed_airports(self,airports):
        for item in airports:
            self.allowed_airports.append(item)


    def connect(self,host,port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
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
    
    def input_message(self):
        self.cont = input("Enter . to quit, press any key to continue ")
        self.dest = input("Destination: ")
        self.payload = input("Passenger Name: ")

    def send(self):
            dest  = self.dest
            payload = self.payload
            #delimiter = '\n'
            message = self.type + '\n' + self.name + '\n' + dest + '\n' + payload + '\n'

            self.sock.send(message.encode(FORMAT))
            #self.sock.send(self.payload.encode(FORMAT))

            self.sock.close()
