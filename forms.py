# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message="Please fill in a valid Email Address")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message="Minimum 6 charachters")])
    submit = SubmitField('Sign Up')
    
    
class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(
            message="This is not a valid Email address")])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')