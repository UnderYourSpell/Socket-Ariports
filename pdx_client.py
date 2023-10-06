from libs.client import Client
from libs.airport_codes import AirportCodes

pdx_client = Client(name = 'PDX')

airports = AirportCodes()

#declare airports we can directly connect to
allowed_airports = ['SEA']
pdx_client.init_allowed_airports(allowed_airports)



while True:
    pdx_client.input_message()
    if pdx_client.cont == '.':
        break
    if pdx_client.dest in allowed_airports:
        #if we have a direct connection to desired airport, connect and send message
        host,port = host,port = airports.get_address(pdx_client.dest)
        pdx_client.connect(host,port)
        pdx_client.send()
    else:
        #Route to Anchorage, Portland is only connected to Seattle
        host,port = host,port = airports.get_address('SEA')
        pdx_client.connect(host,port)
        pdx_client.send()
    