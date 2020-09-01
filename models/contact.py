from utils.hubspot import Hubspot


class Contact():
    id = ""
    firstname = ""
    lastname = ""
    jobtitle = ""
    company_id = None

    #pylint: disable=too-many-arguments
    def __init__(
        self,
        id_c,
        firstname="",
        lastname="",
        jobtitle="",
        email="",
        phone="",
        company_id=None
    ):
        self.id = id_c
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
    def get(id_c):
        contact = Hubspot().crm.contacts.basic_api.get_by_id(
            id_c,associations=['company'], properties=['jobtitle', 'firstname', 'lastname', 'phone', 'email']
        )
        properties = contact.properties
        company_id= None

        if contact.associations is not None and len(contact.associations['companies'].results) > 1:
            company_id=contact.associations['companies'].results[0].id

        return Contact(
            contact.id,
            properties['firstname'],
            properties['lastname'],
            properties['jobtitle'],
            properties['email'],
            properties['phone'],
            company_id
            )

    @staticmethod
    def get_all():
        all_contacts = Hubspot().crm.contacts.get_all()
        return [Contact(contact.id, contact.properties['firstname'], contact.properties['lastname']) for contact in all_contacts]
