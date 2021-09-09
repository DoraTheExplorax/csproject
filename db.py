from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from database.py import db
class users(db.Model):
    id = db.Column('user_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    number = db.Column(db.Integer())
    address = db.Column(db.String(200))
    def __init__(self, name, email, password, number, address):
       self.name = name
       self.email = email
       self.password = password
       self.number = number
       self.address = address
