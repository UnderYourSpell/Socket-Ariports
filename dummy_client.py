from libs.client import Client
from libs.airport_codes import AirportCodes

#This is a dummy client that lets me close all the servers safely
dummy_client = Client(name = 'DUMMY')

airports = AirportCodes()

#declare airports we can directly connect to
allowed_airports = ['ANC','BRW','SEA','PDX','BRW','OTZ','FAI']
dummy_client.init_allowed_airports(allowed_airports)



while True:
    dummy_client.input_message()
    if dummy_client.cont == '.':
        break
    if dummy_client.dest in allowed_airports:
        #if we have a direct connection to desired airport, connect and send message
        host,port = host,port = airports.get_address(dummy_client.dest)
        dummy_client.connect(host,port)
        dummy_client.send()
    