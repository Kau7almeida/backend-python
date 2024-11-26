from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # id (int), username (text), password (text)
    id = db.Column(db.Integer, primary_key = True) # é um inteiro e chave primária
    username = db.Column(db.String(80), nullable = False, unique = True) # é uma string, não pode ser nula e é única
    password = db.Column(db.String(80), nullable = False) # é uma string e não pode ser nula