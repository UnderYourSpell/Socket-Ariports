from libs.server import Server
from libs.airport_codes import AirportCodes
import sys
#Declare a new server
brw = Server(name  = 'BRW')

#Use the name of the airport to find what host/port to use for the server
airports = AirportCodes()
host,port = airports.get_address(brw.name)
brw.bind(host,port)

#tell server what airports we can connect to
client_airports = ['BRW','ANC']
brw.declare_accepted_aiports(client_airports)



#run the server.  It will handle arriving passengers
#as well as facilitating connections
brw.run()

#code here



