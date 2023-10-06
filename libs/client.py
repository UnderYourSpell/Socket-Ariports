import socket

'''
This code supports clients in our system
'''

SIZE = 1024
FORMAT = "utf-8"


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

    def init_allowed_airports(self,airports): #tell the client where it can send something
        #in our client files, the while loop will default mostly to Anchorage
        #PDX defaults to SEA
        for item in airports:
            self.allowed_airports.append(item)


    def connect(self,host,port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_address = (host,port)
        self.host = host
        self.port  = port
        self.sock.connect(server_address)
        print(f"[CONNECTED] Client connected to server at {host}:{port}")

    def update_info(self,dest,payload): #helper function I wrote while testing 
        self.dest = dest
        self.payload = payload

    def dest(self):
        return self.dest
    
    def input_message(self):
        #allows for input from command line
        self.cont = input("Enter . to quit, press any key to continue ")
        self.dest = input("Destination: ")
        self.payload = input("Passenger Name: ")

    def send(self): #send message function
            dest  = self.dest
            payload = self.payload
            #delimiter = '\n'
            #Send the message using delimeters to the server can differentiate what information it recieves
            message = self.type + '\n' + self.name + '\n' + dest + '\n' + payload + '\n'
            print(f"SENDING {payload} TO {dest}")
            self.sock.send(message.encode(FORMAT))
            #self.sock.send(self.payload.encode(FORMAT))

            self.sock.close()
