from utils.hubspot import Hubspot
import sys

class Company():
    id = ""
    name = ""


    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def get(id):
        company = Hubspot().crm.companies.basic_api.get_by_id(id)
        print(company, file=sys.stderr)
        return Company(id, company.properties['name'])
