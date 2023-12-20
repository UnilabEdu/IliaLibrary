from flask import Flask
from flask_admin.contrib.sqla import ModelView

from src.config import Config
from src.extensions import db, login_manager
from src.admin import admin, BookView
from src.commands import init_db_command
from src.models import Book, Author, Series, BookSeries, Theme, BookTheme, Publisher, BookPublisher, Collection, BookCollection


COMMANDS = [
    init_db_command
]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extenstions(app)
    register_commands(app)
    

    return app

def register_extenstions(app):
    db.init_app(app)

    login_manager.init_app(app)

    admin.init_app(app)
    admin.add_view(BookView(Book, db.session))
    admin.add_view(ModelView(Author, db.session))
    admin.add_view(ModelView(Series, db.session))
    admin.add_view(ModelView(Publisher, db.session))
    admin.add_view(ModelView(Theme, db.session))


   
    


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)