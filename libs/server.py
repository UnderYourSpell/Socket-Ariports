import socket
import threading
from .airport_codes import AirportCodes


SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

class Server():

    def __init__(self,sock=None,name  = str):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.server_address = ('',0000)
            self.name  = name
            self.thread_list = []
            self.host = ''
            self.port = 5050
            self.received_payloads = []
            self.connections = []
            self.airport_codes = AirportCodes()
            self.type = "s"
            self.accepted_airports = []

    def declare_accepted_aiports(self,airports):
        for code in airports:
            self.accepted_airports.append(code)

    def bind(self,host,port):
        self.server_address = (host,port)
        self.host = host
        self.port = port
        self.sock.bind(self.server_address)

    def handle_client(self,conn,addr): #will handle multiple client connections at once
        delimiter = '\n'
        print(f"[NETWORK CONNECTION] {addr} connected.")

        #connected  = True

        '''
        If server receives a specific type of information, we handle it a certain way
        So if we are just receiving a payload
        This should carry it's source, and string payload, but should have a delimiter or something to
        say hey, lets just store this information and close the connection because its 
        coming from another server, not a client

        same goes for information coming from a client
        much of the code that does that is already written
        '''
        
        data = conn.recv(SIZE).decode()
        info = data.split(delimiter)
        from_type = info[0]
        name  = info[1]
        dest = info[2]
        payload = info[3]
        
        print(f"{name} CONNECTED")
        print(f"Destination: {dest}")
        
        #handle from a server
        if from_type == "s":
            self.received_payloads.append([name,payload])
            print(f"[PAYLOAD RECEIVED FROM {name}] : {payload}")
            print(self.received_payloads)
        else:

        #dest = conn.recv(SIZE).decode(FORMAT)
        #payload = conn.recv(SIZE).decode(FORMAT)

            self.connections.append(name)
            #code to stop having more than two airport codes references in connections
            list(set(self.connections))
                
            #print(self.connections)

            for airport in self.accepted_airports:
                    if dest == airport:
                        target_host, target_port = self.airport_codes.get_address(dest)
                        target_server = target_host,target_port
                        try:
                            print("[CONNECTING TO DESTINATION]")
                            temp = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #open a tempoerary socket to send the payload to the target client
                            temp.connect(target_server)

                            #send name
                            message = self.type + '\n' + name + '\n' + dest + '\n' + payload + '\n'
                            temp.send(message.encode(FORMAT))
                            temp.close()

                        except Exception as e:
                            print(f"Error sending message: {e}")
                        
        conn.close()

    def run(self):
        print("Starting server")
        self.sock.listen()
        print(f"Listenting on {self.host}:{self.port}")


        while True:
            conn, addr = self.sock.accept()
            new_thread = threading.Thread(target = self.handle_client, args = (conn,addr))
            #should also pass the list of threads so the handle client can 
            #look through and send to the appropriate connection
            self.thread_list.append(new_thread)
            new_thread.start()
            #add thread client to list
            print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')