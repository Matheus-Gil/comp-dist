import logging
from flask import Flask, jsonify
from models import Profile
from database import db
from auth import auth
from sqlalchemy import select
import datetime

# Application log
logging.basicConfig(format='%(asctime)s - %(message)s', filename="log/app.log", level=logging.INFO)
log = logging.getLogger()

def create_default_user(db, app):
    with app.app_context():
        userAlreadyExists = db.session.execute(select(Profile.id).limit(1)).fetchone()
        if not userAlreadyExists:
            name = app.config.get('DEFAULT_ADMIN_NAME')
            passw = app.config.get('DEFAULT_ADMIN_PASSWORD')
            admail = app.config.get('DEFAULT_ADMIN_EMAIL')
            db.session.add(Profile(id='1', username=name, password=passw, email=admail, registered= datetime.datetime.now()))
            db.session.commit()

def create_app_instance():
    # Web Application name
    app = Flask("Comp Dist")

    # Configuration
    app.config.from_pyfile('cfg/app.cfg', silent=True)
    app.config['FLASK_SECRET'] = app.config.get('SECRET_KEY')
    app.config['BASIC_AUTH_FORCE'] = True
    app.secret_key = app.config.get('SECRET_KEY')

    # Set optional bootswatch theme
    app.config['FLASK_ADMIN_SWATCH'] = 'yeti'

    # adding configuration for using a database
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get('DATABASE')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    create_default_user(db, app)

    return app