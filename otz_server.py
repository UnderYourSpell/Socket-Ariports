from libs.server import Server
from libs.airport_codes import AirportCodes

#Declare a new server
otz = Server(name  = 'OTZ')

#Use the name of the airport to find what host/port to use for the server
airports = AirportCodes()
host,port = airports.get_address(otz.name)
otz.bind(host,port)

#tell server what airports we can connect to
client_airports = ['OTZ','ANC']
otz.declare_accepted_aiports(client_airports)

#run the server.  It will handle arriving passengers
#as well as facilitating connections
otz.run()
