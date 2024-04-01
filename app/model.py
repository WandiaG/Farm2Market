from datetime import datetime
from flask import url_for
from flask_login import UserMixin
from app import db , bcrypt
from .exception import ValidationError

#User Model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password_hash = db.Column(db.String(), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self):
        self.password_hash = bcrypt.generate_password_hash(self.password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def get_url(self):
        return url_for('api.get_user', id=self.id, _external=True)


    def export_data(self):
        return  {
            "username": self.username,
            "email": self.email,
            "created_on": self.created_on,
            "url": self.get_url()
        }


    def import_data(self, data):
        try:
            self.username = data["username"]
            self.email = data["email"]
            self.created_on = data["created_on"]
        except KeyError as e:
                raise ValidationError('Invalid customer: missing ' + e.args[0])
        return self


#Other Models to Created