import os
import hubspot

class Hubspot():
    client = None       
    def __new__(self): 
        if self.client is None:
            self.client = hubspot.Client.create(api_key=os.environ['HUPSPOT_TOKEN'])
        return self.client


