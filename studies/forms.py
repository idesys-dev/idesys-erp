from wtforms import Form, StringField, IntegerField, SelectField
from wtforms.fields.html5 import EmailField, TelField
from wtforms import validators as v

class TypeCreate(Form):
    structure_save = SelectField('L\'organisme est-il déjà défini ?', choices=[
        ("Non", "Non"),
        ("Oui", "Oui")])


class ProspectChoice(Form):
    prospect_choice = SelectField('Sélectionner l\'organisme déjà existant', choices=[
        ("Bonnefon", "Bonnefon"),
        ("EDC", "EDC")])
    structure_type = StringField('Type de la structure', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    year = SelectField('Année', choices=[
        ("2018", "2018"),
        ("2019", "2019"),
        ("2020", "2020")])
    sector = SelectField('Filière', choices=[
        ("Informatique", "Informatique"),
        ("Electronique", "Electronique"),
        ("Thermique", "Thermique")])
    prospection = SelectField('Prospection', choices=[
        ("Prospection", "Prospection"),
        ("Spontanee", "Spontanee")])


class CreateStudy(Form):
    structure_name = StringField('Nom de la structure', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    structuretype = StringField('Type de la structure', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    adress = StringField('Adresse', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    city = StringField('Ville', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    postal_code = IntegerField('Code postal', [v.DataRequired()
    ])
    sector = SelectField('Secteur d\'activité', choices=[
        ("Informatique", "Informatique"),
        ("Electronique", "Electronique"),
        ("Thermique", "Thermique")])
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
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    year = SelectField('Année', choices=[
        ("2018", "2018"),
        ("2019", "2019"),
        ("2020", "2020")])
    sector = SelectField('Filière', choices=[
        ("Informatique", "Informatique"),
        ("Electronique", "Electronique"),
        ("Thermique", "Thermique")])
    prospection = SelectField('Prospection', choices=[
        ("Prospection", "Prospection"),
        ("Spontanee", "Spontanee")])
