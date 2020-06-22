from wtforms import Form, StringField, FloatField, validators

class GenerateRM(Form):
    consultant_name = StringField('Nom du consultant', [
        validators.Length(min=0, max=50),
        validators.DataRequired()
    ])
    ref = StringField('Référence', [
        validators.Length(min=0, max=50),
        validators.DataRequired()
    ])

class GenerateBV(Form):
    pay = FloatField('Rémunération brute', [
        validators.DataRequired()
    ])
    jeh = FloatField('Nombre de JEH', [
        validators.DataRequired()
    ])
    ref = StringField('Référence', [
        validators.Length(min=0, max=50),
        validators.DataRequired()
    ])

class GeneratePP(Form):
    client_name = StringField('Nom du client', [
        validators.Length(min=0, max=50),
        validators.DataRequired()
    ])
    ref = StringField('Référence', [
        validators.Length(min=0, max=50),
        validators.DataRequired()
    ])
