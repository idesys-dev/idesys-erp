import os
import hubspot

class Hubspot():
    client = None       
    def __new__(self): 
        if self.client is None:
            self.client = hubspot.Client.create(api_key=os.environ['HUBSPOT_TOKEN'])
        return self.client
