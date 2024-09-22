from app import create_app_instance
from flask_admin import Admin
from database import db
from views import ProfileView
from models import Profile
from app.router import init_router

app = create_app_instance()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        # Admin setup
        admin = Admin(app, name='Super App', template_mode='bootstrap4')
        admin.add_view(ProfileView(Profile, db.session))

        init_router()

    app.run(host="0.0.0.0", debug=True, port=8080)
