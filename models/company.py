from utils.hubspot import Hubspot

class Company():
    id = ""
    name = ""

    def __init__(self, id_h, name):
        self.id = id_h
        self.name = name

    @staticmethod
    def get(id_h):
        company = Hubspot().crm.companies.basic_api.get_by_id(id_h)
        return Company(id_h, company.properties['name'])
