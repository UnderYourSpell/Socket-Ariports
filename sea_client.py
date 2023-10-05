from libs.client import Client
from libs.airport_codes import AirportCodes

sea_client = Client(tier = 4, name = 'SEA')

airports = AirportCodes()
#host,port = airports.get_address('ANC') #connecting to Anchorage


#will do an initial connection to ANC and FAI to let their servers know that we are a client
#peer_airports = ['SEA','ANC','FAI'] #need to tell our own server we exist
#for peer in peer_airports:
    #host,port = airports.get_address(peer)
    #sea_client.connect(host,port)

 #since it is tier 4, we are only connecting to Anchorage

sea_client.update_info("FAI","Jan Ronner")
#sea_client.dest()
host,port = airports.get_address("ANC")
sea_client.connect(host,port)

sea_client.run()
