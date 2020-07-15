from wtforms import Form, StringField, IntegerField, SelectField, TextAreaField
from wtforms.fields.html5 import EmailField, TelField
from wtforms import validators as v
from models.labels import Label
from models.organisme import Organisme

class TypeCreate(Form):
    structure_save = SelectField('L\'organisme est-il déjà défini ?', choices=[
        ("Oui", "Oui"),
        ("Non", "Non")])


class ProspectChoice(Form):
    prospect_choice = SelectField('Sélectionner l\'organisme déjà existant', choices=Organisme.getOrganisme())


class CreateStudy(Form):
    study_name = StringField('Nom de l\'étude', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    follower_study = SelectField('Suiveur d\'étude', choices=[
        ("Aucun", "Aucun"),
        ("Paul Terrassin", "Paul Terrassin"),
        ("David Thibaut", "David Thibaut")])
    follower_quality = SelectField('Suiveur qualité', choices=[
        ("Aucun", "Aucun"),
        ("Ulysse Guyon", "Ulysse Guyon"),
        ("Antoine Zuber", "Antoine Zuber")])
    description = TextAreaField('Description', [
        v.DataRequired()
    ])


class CreateProspect(Form):
    structure_name = StringField('Nom de la structure', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    structure_type = StringField('Type de la structure', [
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
    postal_code = IntegerField('Code postal', [
        v.DataRequired()
    ])
    sector = SelectField('Secteur d\'activité', choices=Label.getLabels("Secteur"))

class CreateContact(Form):
    name = StringField('Nom', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    first_name = StringField('Prénom', [
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
        v.Length(min=0, max=14),
        v.DataRequired()
    ])

class Labels(Form):
    year = SelectField('Année', choices=Label.getLabels("Année"))
    sector = SelectField('Filière', choices=Label.getLabels("Filière"))
    prospection = SelectField('Prospection', choices=Label.getLabels("Prospection"))
