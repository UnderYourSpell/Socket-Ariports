from libs.client import Client
from libs.airport_codes import AirportCodes

otz_client = Client(name = 'OTZ')

airports = AirportCodes()

 #connecting to Anchorage
#will only ever be connected to Ancorage
allowed_airports = ['ANC']
otz_client.init_allowed_airports(allowed_airports)
 #since it is tier 4, we are only connecting to Anchorage


while True:
    otz_client.input_message()
    if otz_client.cont == '.':
        break
    if otz_client.dest in allowed_airports:
        host,port = host,port = airports.get_address(otz_client.dest)
        otz_client.connect(host,port)
        otz_client.send()
    else:
        #default to anchorage, because we know it has connections to all airports
        host,port = host,port = airports.get_address('ANC')
        otz_client.connect(host,port)
        otz_client.send()
    