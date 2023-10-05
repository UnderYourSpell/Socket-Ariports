from libs.server import Server
from libs.airport_codes import AirportCodes

fai = Server(tier = 1,name  = 'FAI')

airports = AirportCodes()
host,port = airports.get_address(fai.name)
fai.bind(host,port)

client_airports = ['ANC','FAI','SEA']
fai.declare_accepted_aiports(client_airports)

fai.run()
