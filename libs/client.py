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
        
    def connect(self,host,port):
        server_address = (host,port)
        self.host = host
        self.port  = port
        self.sock.connect(server_address)
        print(f"[CONNECTED] Client connected to server at {host}:{port}")

    def update_info(self,dest,payload):
        self.dest = dest
        self.payload = payload

    def run(self):
        connected = True
        dest  = self.dest
        payload = self.payload
        delimiter = '\n'

        #send name of client airport
        self.sock.send(self.name.encode(FORMAT))
        self.sock.send(delimiter.encode(FORMAT))

        #send destination
        self.sock.send(dest.encode(FORMAT))
        self.sock.send(delimiter.encode(FORMAT))
        
        #send payload
        self.sock.send(payload.encode(FORMAT))
        self.sock.send(delimiter.encode(FORMAT))
        #self.sock.send(self.payload.encode(FORMAT))

        try:
            while connected:
                
                
                message = input("> ")
                #In message, we will send 3 things, Source, Destination, Payload
                # Encode and send the message to the server
                self.sock.send(message.encode(FORMAT))
                #self.sock.send(message2.encode(FORMAT))

                if message == DISCONNECT_MSG:
                    connected = False
                else:
                    # Receive the response from the server
                    message = self.sock.recv(SIZE).decode(FORMAT)
                    print(f"[SERVER] {message}")


        except Exception as e:
            print("Error: {}".format(e))

        finally:
            # Clean up the connection
            self.sock.close()
