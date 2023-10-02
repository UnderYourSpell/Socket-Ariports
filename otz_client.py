from clients.client_class import Client
from libs.airport_codes import AirportCodes

otz_client = Client(tier = 4, name = 'OTZ')

airports = AirportCodes()
host,port = airports.get_address('ANC') #connecting to Anchorage

otz_client.connect(host,port) #since it is tier 4, we are only connecting to Anchorage

otz_client.run()

