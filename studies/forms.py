from wtforms import Form, StringField, IntegerField, SelectField, TextAreaField
from wtforms.fields.html5 import EmailField, TelField
from wtforms import validators as v
from models import organisme, labels

def getLabels(typeLabel):
    mesLabels = [("Aucun", "Aucun")]
    for item in labels.Label.objects:
        if item.category == typeLabel:
            mesLabels.append((item.label, item.label))
    return mesLabels

def getProspect():
    prospect = [("Aucun", "Aucun")]
    for item in organisme.Organisme.objects:
        prospect.append((item.name, item.name))
    return prospect

class TypeCreate(Form):
    structureSave = SelectField('L\'organisme est-il déjà défini ?', choices=[
        ("Oui", "Oui"),
        ("Non", "Non")])


class ProspectChoice(Form):
    prospectChoice = SelectField('Sélectionner l\'organisme déjà existant', choices=getProspect())


class CreateStudy(Form):
    studyName = StringField('Nom de l\'étude', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    followerStudy = SelectField('Suiveur d\'étude', choices=[
        ("Aucun", "Aucun"),
        ("Paul Terrassin", "Paul Terrassin"),
        ("David Thibaut", "David Thibaut")])
    followerQuality = SelectField('Suiveur qualité', choices=[
        ("Aucun", "Aucun"),
        ("Ulysse Guyon", "Ulysse Guyon"),
        ("Antoine Zuber", "Antoine Zuber")])
    description = TextAreaField('Description', [
        v.DataRequired()
    ])


class CreateProspect(Form):
    structureName = StringField('Nom de la structure', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    structureType = StringField('Type de la structure', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    adresse = StringField('Adresse', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    city = StringField('Ville', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    postalCode = IntegerField('Code postal', [
        v.DataRequired()
    ])
    sector = SelectField('Secteur d\'activité', choices=getLabels("Secteur"))

class CreateContact(Form):
    name = StringField('Nom', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    firstName = StringField('Prénom', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    position = StringField('Poste', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    email = EmailField('Email', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    phone = TelField('Téléphone', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])


class Labels(Form):
    year = SelectField('Année', choices=getLabels("Année"))
    sector = SelectField('Filière', choices=getLabels("Filière"))
    prospection = SelectField('Prospection', choices=getLabels("Prospection"))
