import logging
from flask import Flask, jsonify
from models import Profile
from database import db
from auth import auth


# Application log
logging.basicConfig(format='%(asctime)s - %(message)s', filename="log/app.log", level=logging.INFO)
log = logging.getLogger()

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
    databaseURL = app.config.get('DATABASE')
    if not databaseURL:
        databaseURL = app.config.get('DEFAULT_DATABASE')

    app.config['SQLALCHEMY_DATABASE_URI'] = databaseURL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app