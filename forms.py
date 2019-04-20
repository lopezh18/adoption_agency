from flask_wtf import FlaskForm, validators
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import Optional, url, InputRequired, NumberRange
from flask_debugtoolbar import DebugToolbarExtension


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species",choices=[('porcupine', 'Porcupine'),('dog','Dog'),('cat','Cat')], validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(),url()])
    age = IntegerField("Age", validators=[InputRequired(),NumberRange(min=0, max=30, message='Please provide a number between 0 and 30.')])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Availability")
