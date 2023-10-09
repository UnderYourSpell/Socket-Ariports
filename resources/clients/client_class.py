import socket

class Client:

    def __init__(self,sock=None,tier = int, name = str):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.tier = tier
            self.name = name
    
    def connect(self,host,port):
        server_address = (host, port)
        self.sock.connect(server_address)
    
    def run(self):
        try:
            while True:
                message = input("Enter a message to send to the server (or '.' to quit): ")
                
                if message == '.':
                    break  # Exit and close the connection
                
                # Encode and send the message to the server
                self.sock.sendall(message.encode())

                # Receive the response from the server
                data = self.sock.recv(1024)
                print("Received from server: {}".format(data.decode()))

        except Exception as e:
            print("Error: {}".format(e))

        finally:
            # Clean up the connection
            self.sock.close()