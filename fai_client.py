from libs.client import Client
from libs.airport_codes import AirportCodes

fai_client = Client(tier = 4, name = 'FAI')

airports = AirportCodes()
host,port = airports.get_address('ANC') #connecting to Anchorage

fai_client.connect(host,port) #since it is tier 4, we are only connecting to Anchorage

fai_client.update_info("ANC","Moro Bamber")

fai_client.run()

