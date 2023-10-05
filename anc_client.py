from libs.client import Client
from libs.airport_codes import AirportCodes

anc_client = Client(tier = 4, name = 'ANC')

airports = AirportCodes()
host,port = airports.get_address('ANC') #connecting to Anchorage

anc_client.connect(host,port) #since it is tier 4, we are only connecting to Anchorage
peer_airports = ['ANC','FAI','SEA']
for peer in peer_airports:
    anc_client.connect(airports.get_address(peer))


anc_client.update_info("FAI","Moro Bamber")

host,port = airports.get_address(anc_client.dest())
anc_client.run()
