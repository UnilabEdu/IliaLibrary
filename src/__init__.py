from flask import Flask

from src.config import Config
from src.extensions import db, login_manager, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extenstions(app)
    

    return app

def register_extenstions(app):
    db.init_app(app)

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


