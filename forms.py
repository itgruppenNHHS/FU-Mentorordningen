from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, validators

def CheckNameLength(form, field):
  if len(field.data) < 4:
    raise ValidationError('Name must have more then 3 characters')

class ContactForm(Form):
    emne = StringField('Emne:', [validators.DataRequired(), CheckNameLength])
    message = TextAreaField('Din melding:', [validators.DataRequired()])
    submit = SubmitField('Send')

