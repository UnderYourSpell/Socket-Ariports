from libs.client import Client
from libs.airport_codes import AirportCodes

anc_client = Client(name = 'ANC')

airports = AirportCodes()

#declare airports we can directly connect to
allowed_airports = ['FAI','SEA','BRW','OTZ']
anc_client.init_allowed_airports(allowed_airports)



while True:
    anc_client.input_message()
    if anc_client.cont == '.':
        break
    if anc_client.dest in allowed_airports:
        #if we have a direct connection to desired airport, connect and send message
        host,port = host,port = airports.get_address(anc_client.dest)
        anc_client.connect(host,port)
        anc_client.send()
    else:
        #Route to Anchorage, Anchorage is connected to all airports
        host,port = host,port = airports.get_address('ANC')
        anc_client.connect(host,port)
        anc_client.send()
    