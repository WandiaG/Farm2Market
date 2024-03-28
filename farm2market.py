from flask import Flask, render_template
import requests
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farmdata.db'
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))
  email = db.Column(db.String(120), unique=True)  # Enforce unique email addresses
  password = db.Column(String(60))  # Consider using a password hashing mechanism for security

@app.route("/")
def home():
    users = User.query.all()
    for user in users:
        print({user.name})
    return "<h1> Farm Freshness {user.name} </h1>"

if __name__ == '__main__':
    app.run(debug=True)