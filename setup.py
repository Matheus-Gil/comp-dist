from app import create_app_instance
from flask_admin import Admin
from database import db
from views import ProfileView
from models import Profile
from app.router import init_router
from sqlalchemy import select
import datetime

app = create_app_instance()

def create_default_user(db, app):
    #with app.app_context():
    userAlreadyExists = db.session.execute(select(Profile.id).limit(1)).fetchone()
    if not userAlreadyExists:
        name = app.config.get('DEFAULT_ADMIN_NAME')
        passw = app.config.get('DEFAULT_ADMIN_PASSWORD')
        admail = app.config.get('DEFAULT_ADMIN_EMAIL')
        db.session.add(Profile(id='1', username=name, password=passw, email=admail, registered= datetime.datetime.now()))
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        create_default_user(db, app)

        # Admin setup
        admin = Admin(app, name='Super App', template_mode='bootstrap4')
        admin.add_view(ProfileView(Profile, db.session))

        init_router()

    app.run(host="0.0.0.0", debug=True, port=8080)
