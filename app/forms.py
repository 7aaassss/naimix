from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField, StringField
from wtforms.validators import DataRequired

class manForm(FlaskForm):
    date_birth = DateField('birth', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    submit = SubmitField('Continue')