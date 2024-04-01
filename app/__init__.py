import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
    app.config.from_pyfile(cfg)
    db.init_app(app)
    bcrypt.init_app(app)

    from app.api_v1 import api
    app.register_blueprint(api)

    return app
