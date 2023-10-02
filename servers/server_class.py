import socket


class Server():

    def __init__(self,sock=None,tier = int,name  = str):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.server_address = ('',0000)
            self.tier = tier
            self.name  = name
            self.arrived = []

    def bind(self,host,port):
        self.server_address = (host,port)
        self.sock.bind(self.server_address)  

    def run(self):
        self.sock.listen(5)

        print("Server is listening on {}.{}".format(*self.server_address))

        print("TCP server is waiting for incoming connections")

        while True:
            #Wait for connection from client
            print("Waiting for a connection...")
            client_socket, client_address = self.sock.accept()
            print("Accepted connection from {}:{}".format(*client_address))

            try:
                while True:
                    # Receive data from the client
                    data = client_socket.recv(1024)
                    if not data:
                        break  # No more data, break the loop
        
                    # Decode the received data, format with the variables involved, and display the string.
                    print(f"Received data from {client_address}: {data.decode()}")

                    if data.decode() == self.name:
                        print('You have arrived')
                        self.arrived.append(data.decode())
                    else:
                        print('Forwarding to destination')
            
                    # Create an acknowledgment.
                    ack = "Hey, this is the server acknowledging the receipt of your data: " + data.decode()

                    # Encode the acknowledgment and send to client.
                    client_socket.sendall(ack.encode())
            except Exception as e:
                print("Error: {}".format(e))
            finally:
                # Clean up the connection
                client_socket.close()
                print("Connection closed by {}:{}".format(*client_address))
