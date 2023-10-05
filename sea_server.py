from libs.server import Server
from libs.airport_codes import AirportCodes

sea = Server(tier = 1,name  = 'SEA')

airports = AirportCodes()
host,port = airports.get_address(sea.name)
sea.bind(host,port)

client_airports = ['ANC','FAI','SEA']
sea.declare_accepted_aiports(client_airports)

sea.run()
