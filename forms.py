from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class registration_form(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min = 6, max = 15)])

    email = StringField('Email', validators = [DataRequired(), Email()])

    password = PasswordField('Password', validators = [DataRequired()])
    
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign up')


class login_form(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])

    password = PasswordField('Password', validators = [DataRequired()])

    remember = BooleanField('Stay signed in')

    submit = SubmitField('Login')