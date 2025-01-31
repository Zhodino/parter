from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired, Email
from wtforms.fields import EmailField

from wtforms import ValidationError
import re


def validate_phone(form, field):
    phone_pattern = re.compile(r'^\+\d{11,15}$')
    if not phone_pattern.match(field.data):
        raise ValidationError('Invalid phone number. Please enter in the format: +12345678901')


class LoginForm(FlaskForm):
    username = StringField('Phone/Email')
    password = PasswordField("Password")
    login = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username')
    email = EmailField('Email Address', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), validate_phone])
    password = PasswordField("Password")
    conf_password = PasswordField("Confirm Password")
    register = SubmitField('Register')


class NothingForm(FlaskForm):
        pass
