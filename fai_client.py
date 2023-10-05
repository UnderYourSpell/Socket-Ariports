from libs.client import Client
from libs.airport_codes import AirportCodes

fai_client = Client(tier = 4, name = 'FAI')
airports = AirportCodes()


#we need an initial connection thing
 #since it is tier 4, we are only connecting to Anchorage
fai_client.update_info("SEA","Moro Bamber")

host,port = airports.get_address('SEA') #connecting to where we have dest set to

fai_client.connect(host,port)
fai_client.run()

