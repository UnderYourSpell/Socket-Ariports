from libs.client import Client
from libs.airport_codes import AirportCodes

sea_client = Client(name = 'SEA')

airports = AirportCodes()

#declare airports we can directly connect to
allowed_airports = ['ANC','PDX','FAI']
sea_client.init_allowed_airports(allowed_airports)



while True:
    sea_client.input_message()
    if sea_client.cont == '.':
        break
    if sea_client.dest in allowed_airports:
        #if we have a direct connection to desired airport, connect and send message
        host,port = host,port = airports.get_address(sea_client.dest)
        sea_client.connect(host,port)
        sea_client.send()
    else:
        #Route to Anchorage, Anchorage is connected to all airports
        host,port = host,port = airports.get_address('ANC')
        sea_client.connect(host,port)
        sea_client.send()
    