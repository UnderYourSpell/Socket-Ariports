from libs.server import Server
from libs.airport_codes import AirportCodes
import sys

#Declare a new server
anc = Server(name  = 'ANC')

#Use the name of the airport to find what host/port to use for the server
airports = AirportCodes()
host,port = airports.get_address(anc.name)
anc.bind(host,port)

output_file_name = "anc_server_output.txt"

with open(output_file_name, "w") as output_file:
    sys.stdout = output_file

    #tell server what airports we can connect to
    client_airports = ['ANC','SEA','FAI','BRW','OTZ']
    anc.declare_accepted_aiports(client_airports)

    #run the server.  It will handle arriving passengers
    #as well as facilitating connections
    anc.run()

    #code here

output_file.close()




