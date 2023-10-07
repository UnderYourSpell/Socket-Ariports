from libs.server import Server
from libs.airport_codes import AirportCodes
import sys
#Declare a new server
sea = Server(name  = 'SEA')

#Use the name of the airport to find what host/port to use for the server
airports = AirportCodes()
host,port = airports.get_address(sea.name)
sea.bind(host,port)

#tell server what airports we can connect to
client_airports = ['SEA','ANC','FAI','PDX']
sea.declare_accepted_aiports(client_airports)

output_file_name = "xxx_server_output.txt"

with open(output_file_name, "w") as output_file:
    sys.stdout = output_file

    #run the server.  It will handle arriving passengers
    #as well as facilitating connections
    sea.run()
    #code here

output_file.close()


