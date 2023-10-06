from libs.client import Client
from libs.airport_codes import AirportCodes

brw_client = Client(name = 'BRW')

airports = AirportCodes()

#declare airports we can directly connect to
allowed_airports = ['ANC','FAI']
brw_client.init_allowed_airports(allowed_airports)



while True:
    brw_client.input_message()
    if brw_client.cont == '.':
        break
    if brw_client.dest in allowed_airports:
        #if we have a direct connection to desired airport, connect and send message
        host,port = host,port = airports.get_address(brw_client.dest)
        brw_client.connect(host,port)
        brw_client.send()
    else:
        #Route to Anchorage, Anchorage is connected to all airports
        host,port = host,port = airports.get_address('ANC')
        brw_client.connect(host,port)
        brw_client.send()
    