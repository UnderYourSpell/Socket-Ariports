import socket
import threading
from .airport_codes import AirportCodes

'''
This code supports the servers in our system
'''


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
            self.run_server = 1

    def declare_accepted_aiports(self,airports): #tell the server what airports it can connect to
        for code in airports:
            self.accepted_airports.append(code)

    def bind(self,host,port): #bind to a port
        self.server_address = (host,port)
        self.host = host
        self.port = port
        self.sock.bind(self.server_address)

    def handle_client(self,conn,addr): #will handle multiple client connections at once
        delimiter = '\n'
        print(f"[NETWORK CONNECTION] {addr} connected.")

        #receive the data, and parse the information that was sent
        data = conn.recv(SIZE).decode()
        info = data.split(delimiter)
        from_type = info[0]
        name  = info[1]
        dest = info[2]
        payload = info[3]

        #Allows me to stop the server from running so I can save the Log file
        if payload == '!END_SERVER':
                print("[SERVER STOP REQUEST RECEIVED]")
                print("[STOPPING SERVER]")
                self.run_server = 0

        #Show who's connected and what their destination i
        print(f"{name} CONNECTED")
        print(f"DESTINATION: {dest}")
        
        '''handle from a server
        in my server architecture, since we only have 1 layover
        if a server forwards something, then the next server that receives it will
        store the info

        This server also recognizes itself as a client so it can forward a message to itself
        ''' 
        if from_type == "s":
            self.received_payloads.append([name,payload])
            print(f"{payload} HAS ARRIVED IN: {dest} FROM: {name}")
            print(self.received_payloads)
        else:

        #dest = conn.recv(SIZE).decode(FORMAT)
        #payload = conn.recv(SIZE).decode(FORMAT)

            self.connections.append(name)
            #code to stop having more than two airport codes references in connections
            list(set(self.connections))
                
            #print(self.connections)

            #if the airport exists in what airports we can go to
            #send a message as a new client
            #it connects the passenger to the final destination
            for airport in self.accepted_airports:
                    if dest == airport:
                        target_host, target_port = self.airport_codes.get_address(dest)
                        target_server = target_host,target_port
                        try:
                            print(f"CONNECTING PASSENGER {payload} TO {dest}")
                            temp = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #open a tempoerary socket to send the payload to the target client
                            temp.connect(target_server)

                            #send name
                            message = self.type + '\n' + name + '\n' + dest + '\n' + payload + '\n'
                            temp.send(message.encode(FORMAT))
                            temp.close()

                        except Exception as e:
                            print(f"Error sending message: {e}")
                        
        conn.close()

    def run(self): #starts the server's listenting function
        #allows for multiple connections
        print("Starting server")
        self.sock.listen()
        print(f"Listenting on {self.host}:{self.port}")

        #main body that accepts things into the server
        #uses the client handle function to do server operations
        while self.run_server == 1:
            conn, addr = self.sock.accept()
            new_thread = threading.Thread(target = self.handle_client, args = (conn,addr))
            #should also pass the list of threads so the handle client can 
            #look through and send to the appropriate connection
            self.thread_list.append(new_thread)
            new_thread.start()
            #add thread client to list
        
        self.sock.close()