# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120))
    pwhash = db.Column(db.String(54))
    
    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.set_password(password)
        
    def set_password(self, password):
        self.pwhash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.pwhash, password)
