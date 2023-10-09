import sys
import socket
import threading
import time

QUIT = False

class ClientThread( threading.Thread ):

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

class Server:
    ''' 
    Server class. Opens up a socket and listens for incoming connections.
    Every time a new connection arrives, it creates a new ClientThread thread
    object and defers the processing of the connection to it. 
    '''

    def __init__(self,sock=None,tier = int,name  = str):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.server_address = ('',0000)
            self.tier = tier
            self.name  = name
            self.arrived = []
            self.thread_list = []

    def bind(self,host,port):
        self.server_address = (host,port)
        self.sock.bind(self.server_address)          

    def run( self ):
        '''
        Server main loop. 
        Creates the server (incoming) socket, and listens on it of incoming
        connections. Once an incomming connection is deteceted, creates a 
        ClientThread to handle it, and goes back to listening mode.
        '''
        all_good = False
        try_count = 0

        #
        # Attempt to open the socket
        #
        while not all_good:
            if 3 < try_count:
                #
                # Tried more than 3 times, without success... Maybe the port
                # is in use by another program
                #
                sys.exit( 1 )
            try:
                #
                # Create the socket
                #
                self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
                #
                # Bind it to the interface and port we want to listen on
                #
                self.bind(self.server_address)
                #
                # Listen for incoming connections. This server can handle up to
                # 5 simultaneous connections
                #
                self.sock.listen( 5 )
                all_good = True
                break
            except socket.error as err:
                #
                # Could not bind on the interface and port, wait for 10 seconds
                #
                print ('Socket connection error... Waiting 10 seconds to retry.')
                del self.sock
                time.sleep( 10 )
                try_count += 1

        print ("Server is listening for incoming connections.")
        print ("Try to connect through the command line, with:")
        print ("telnet localhost 5050")
        print ("and then type whatever you want.")
        print
        print ("typing 'bye' finishes the thread, but not the server ")
        print ("(eg. you can quit telnet, run it again and get a different ")
        print ("thread name")
        print ("typing 'quit' finishes the server")

        try:
            #
            # NOTE - No need to declare QUIT as global, since the method never 
            #    changes its value
            #
            while not QUIT:
                try:
                    #
                    # Wait for half a second for incoming connections
                    #
                    self.sock.settimeout( 0.500 )
                    client = self.sock.accept()[0]
                except socket.timeout:
                    #
                    # No connection detected, sleep for one second, then check
                    # if the global QUIT flag has been set
                    #
                    time.sleep( 1 )
                    if QUIT:
                        print ("Received quit command. Shutting down...")
                        break
                    continue
                #
                # Create the ClientThread object and let it handle the incoming
                # connection
                #
                new_thread = ClientThread( client )
                print ('Incoming Connection. Started thread ')
                print (new_thread.getName())
                self.thread_list.append( new_thread )
                new_thread.start()

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
                        #
                        # Go over the list of threads, remove those that have finished
                        # (their run method has finished running) and wait for them 
                        # to fully finish
                        #
                        for thread in self.thread_list:
                            if not thread.is_alive():
                                self.thread_list.remove( thread )
                                thread.join()

        except KeyboardInterrupt:
            print ('Ctrl+C pressed... Shutting Down')
        except Exception as err:
            print (f"Exception caught: {err}\nClosing...") #change this?

        #
        # Clear the list of threads, giving each thread 1 second to finish
        # NOTE: There is no guarantee that the thread has finished in the
        #    given time. You should always check if the thread isAlive() after
        #    calling join() with a timeout paramenter to detect if the thread
        #    did finish in the requested time
        #
        for thread in self.thread_list:
            thread.join( 1.0 )
        #
        # Close the socket once we're done with it
        #
        self.sock.close()

if "__main__" == __name__:
    server = Server()
    server.run()

    print ("Terminated")