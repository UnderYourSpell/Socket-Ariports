

class AirportCodes():

    def __init__(self):
        self.table = {'ANC' : ['localhost',8080],
                      'FAI' : ['localhost',8081],
                      'SEA': ['localhost',8082],
                      'BRW': ['localhost',8083],
                      'OTZ': ['localhost',8084]}
    
    def get_address(self,code):
        try:
            address = self.table[code]
            hostname, port = address
            return hostname, port
        except:
            print("Airport code not found")