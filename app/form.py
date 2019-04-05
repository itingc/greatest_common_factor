from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    num1 = StringField('First Number', validators=[DataRequired()])
    num2 = StringField('Second Number', validators=[DataRequired()])
    result = SubmitField('Calculate GCF')
    #reset = SubmitField('Clear')