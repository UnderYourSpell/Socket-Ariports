from libs.server import Server
from libs.airport_codes import AirportCodes

#Declare a new server
fai = Server(name  = 'FAI')

#Use the name of the airport to find what host/port to use for the server
airports = AirportCodes()
host,port = airports.get_address(fai.name)
fai.bind(host,port)

#tell server what airports we can connect to
client_airports = ['FAI','SEA','ANC']
fai.declare_accepted_aiports(client_airports)

#run the server.  It will handle arriving passengers
#as well as facilitating connections
fai.run()
