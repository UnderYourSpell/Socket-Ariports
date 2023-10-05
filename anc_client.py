from libs.client import Client
from libs.airport_codes import AirportCodes

anc_client = Client(tier = 1)

airports = AirportCodes()
host,port = airports.get_address('ANC')

anc_client.connect(host,port)

anc_client.run()

