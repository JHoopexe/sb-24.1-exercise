
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, URLField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange

class AddPet(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired()])
    image = URLField("Photo URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])

class EditPet(FlaskForm):
    notes = StringField("Notes", validators=[Optional()])
    available = SelectField("Available", choices=[('true', 'Yes'), ('false', 'No')])
