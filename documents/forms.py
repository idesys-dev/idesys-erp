from wtforms import Form, StringField, FloatField, IntegerField, DateField, SelectField
from wtforms import validators as v

class GenerateRM(Form):
    consultant_name = StringField('Nom du consultant', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    ref = StringField('Référence', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])

class GenerateBV(Form):
    pay = FloatField('Rémunération brute', [
        v.DataRequired()
    ])
    jeh = FloatField('Nombre de JEH', [
        v.DataRequired()
    ])
    ref = StringField('Référence', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])

class GeneratePP(Form):
    client_name = StringField('Nom du client', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])
    ref = StringField('Référence', [
        v.Length(min=0, max=50),
        v.DataRequired()
    ])

class GenerateFA(Form):
    reference = StringField('Référence', [ v.Length(min=0, max=50),
        v.DataRequired()])
    client_name = StringField('Nom du client', [ v.Length(min=0, max=50),
        v.DataRequired()])
    client_address = StringField('Adresse du client', [ v.Length(min=0, max=250),
        v.DataRequired()])
    no_etude = IntegerField("Numéro de l'étude", [v.DataRequired()])
    contract_type = SelectField('Type de contrat', choices=[
        ("Convention d'Étude", "Convention d'Étude"),
        ("Convention Cadre", "Convention Cadre")])
    reference_contract = StringField('Réfécence du contrat',
        [v.Length(min=0, max=50), v.DataRequired()])
    fees = FloatField('Frais', [v.DataRequired()], default=100)
    issue_date = DateField("Date d'émission", [v.DataRequired()], format='%d/%m/%Y')
    expiry_date = DateField("Date d'échéance", format='%d/%m/%Y')
    percentage_deposit = IntegerField("Pourcentage de l'acompte",
        [v.NumberRange(min=1, max=99), v.DataRequired()])
