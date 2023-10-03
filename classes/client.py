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
        
    def connect(self,host,port):
        server_address = (host,port)
        self.host = host
        self.port  = port
        self.sock.connect(server_address)
        print(f"[CONNECTED] Client connected to server at {host}:{port}")

    def run(self):
        connected = True
        try:
            while connected:
                message = input("> ")

                # Encode and send the message to the server
                self.sock.send(message.encode(FORMAT))

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
