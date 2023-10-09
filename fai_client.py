from libs.client import Client
from libs.airport_codes import AirportCodes

fai_client = Client(name = 'FAI')

airports = AirportCodes()

#declare airports we can directly connect to
allowed_airports = ['ANC','SEA']
fai_client.init_allowed_airports(allowed_airports)



while True:
    fai_client.input_message()
    if fai_client.cont == '.':
        break
    if fai_client.dest in allowed_airports:
        #if we have a direct connection to desired airport, connect and send message
        host,port = host,port = airports.get_address(fai_client.dest)
        fai_client.connect(host,port)
        fai_client.send()
    elif fai_client.dest == 'PDX':
        host,port = host,port = airports.get_address('SEA')
        fai_client.connect(host,port)
        fai_client.send()
    else:
        #Route to Anchorage, Anchorage is connected to all airports
        host,port = host,port = airports.get_address('ANC')
        fai_client.connect(host,port)
        fai_client.send()
    