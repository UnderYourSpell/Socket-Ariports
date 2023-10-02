from servers.server_class import Server
from libs.airport_codes import AirportCodes

anc = Server()
airports = AirportCodes()
host,port = airports.get_address('ANC')

anc.bind(host,port)

anc.sock.listen(5)

print("Server is listening on{}.{}".format(*anc.server_address))

print("TCP server is waiting for incoming connections")

while True:
    #Wait for connection from client
    print("Waiting for a connection...")
    client_socket, client_address = anc.sock.accept()
    print("Accepted connection from {}:{}".format(*client_address))

    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break  # No more data, break the loop
  
            # Decode the received data, format with the variables involved, and display the string.
            print(f"Received data from {client_address}: {data.decode()}")
    
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