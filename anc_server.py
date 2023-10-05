from libs.server import Server
from libs.airport_codes import AirportCodes

anc = Server(tier = 1,name  = 'ANC')

airports = AirportCodes()
host,port = airports.get_address(anc.name)
anc.bind(host,port)

client_airports = ['ANC','FAI','SEA','OTZ']
anc.declare_accepted_aiports(client_airports)

anc.run()
