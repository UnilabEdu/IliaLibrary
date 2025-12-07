from flask import Flask

from src.config import Config
from src.extensions import db, login_manager, migrate
from src.admin import admin, BookView, GenericView, UserView
from src.admin.book import SecureModelView
from src.commands import init_db_command, populate_db_command
from src.models import MediaType, Language, Genre, Book, BookContent, User
from src.views import auth_blueprint, main_blueprint

COMMANDS = [
    init_db_command,
    populate_db_command
]

BLUEPRINTS = [
    auth_blueprint,
    main_blueprint
]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extenstions(app)
    register_commands(app)
    register_blueprints(app)

    return app


def register_extenstions(app):
    db.init_app(app)

    migrate.init_app(app, db)

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    admin.init_app(app)

    admin.add_view(UserView(User, db.session, name="მომხმარებელი"))
    admin.add_view(BookView(Book, db.session, name="წიგნები"))
    admin.add_view(GenericView(MediaType, db.session, name="მედიის ტიპი", category="ფილტრაცია"))
    admin.add_view(GenericView(Genre, db.session, name="ჟანრი", category="ფილტრაცია"))
    admin.add_view(GenericView(Language, db.session, name="ენა", category="ფილტრაცია"))



def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
