from wtforms import Form, StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.fields.html5 import EmailField, TelField
from wtforms import validators as v
from models.labels import Labels
from models.user import User
from flask_wtf import FlaskForm


class TypeCreate(Form):
    structure_save = SelectField('L\'organisme est-il déjà défini ?', choices=[
        ("Oui", "Oui"),
        ("Non", "Non")])

class ProspectChoice(Form):
    prospect_choice = SelectField('Sélectionner l\'organisme déjà existant')

class CreateStudy(Form):
    study_name = StringField('Nom de l\'étude', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])

    follower_study = SelectField('Suiveur d\'étude', choices=User.get_admin_intervener(True))

    follower_quality = SelectField('Suiveur qualité', choices=User.get_admin_intervener(True))

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

    sector = SelectField('Secteur d\'activité', choices=Labels.get_labels("Secteur"))

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

class LabelsForm(Form):
    year = SelectField('Année', choices=Labels.get_labels("Année"))
    sector = SelectField('Filière', choices=Labels.get_labels("Filière"))
    prospection = SelectField('Prospection', choices=Labels.get_labels("Prospection"))

class CreatePhases(FlaskForm):
    name = StringField('Nom', validators=[
        v.Length(min=5, max=50, message="Entre 5 et 50 caractères"),
        v.DataRequired()
    ])
    description = TextAreaField('Description',  validators=[
        v.Length(min=0, max=150),
        v.DataRequired()
    ])
    lenght_week = IntegerField('Durée en semaine',  validators=[
        v.DataRequired()
    ])
    nb_jeh = IntegerField('Nombre de JEH',  validators=[
        v.DataRequired()
    ])
    price_jeh = IntegerField('Prix d\'une JEH',  validators=[
        v.NumberRange(min=80, max=400, message="JEH compris entre 80 & 400 €"),
        v.DataRequired()
    ])
    phase_number = IntegerField('Numéro de phase',  validators=[
        v.DataRequired()
    ])

    control_point = BooleanField('Point de controle')

    bill = BooleanField('Facture')