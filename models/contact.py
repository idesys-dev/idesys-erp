from utils.hubspot import Hubspot
import sys

class Contact():
    id = ""
    firstname = ""
    lastname = ""
    jobtitle = ""
    company_id = ""

    def __init__(self, id, firstname="", lastname="", jobtitle="", email="", phone="", company_id=""):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.jobtitle = jobtitle
        self.email = email
        self.phone = phone
        self.company_id = company_id

    def get_name(self):
        s = self.id+") "
        if self.firstname:
            s += self.firstname+" "
        if self.lastname:
            s += self.lastname
        return s

    @staticmethod
    def get(id):
        contact = Hubspot().crm.contacts.basic_api.get_by_id(id,associations=['company'], properties=['jobtitle', 'firstname', 'lastname', 'phone', 'email'])
        print(contact, file=sys.stderr)
        properties = contact.properties
        return Contact(contact.id, properties['firstname'], properties['lastname'], properties['jobtitle'], properties['email'], properties['phone'], company_id=contact.associations['companies'].results[0].id)

    @staticmethod
    def get_all():
        all = Hubspot().crm.contacts.get_all()
        return [Contact(contact.id, contact.properties['firstname'], contact.properties['lastname']) for contact in all]


