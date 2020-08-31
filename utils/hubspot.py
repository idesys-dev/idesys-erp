import os
from hubspot import HubSpot

class Hubspot():
    client = None       
    def __new__(self): 
        if self.client is None:
            self.client = HubSpot(api_key=os.environ['HUBSPOT_TOKEN'])
        return self.client
