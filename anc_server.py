from classes.server import Server
from libs.airport_codes import AirportCodes

anc = Server(tier = 1,name  = 'ANC')

airports = AirportCodes()
host,port = airports.get_address(anc.name)

anc.bind(host,port)

anc.run()
