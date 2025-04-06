from flask.cli import with_appcontext
import click

from src.models import User, Book, MediaType, Language, Genre
from src.extensions import db


@click.command("init_db")
@with_appcontext
def init_db_command():
    click.echo("Database creation in porgress")

    db.drop_all()
    db.create_all()

    click.echo("Database created")


@click.command("populate_db")
@with_appcontext
def populate_db_command():
    click.echo("Populating Users")
    user1 = User(username="admin", password="admin123")
    user1.password = "admin123"
    user1.create()

    click.echo("Populating Media types")
    media_types = ["წიგნები", "პერიოდიცა", "წერილები", "ხელნაწერები", "აუდიო", "ფოტო"]
    for media in media_types:
        MediaType(name=media).create()

    click.echo("Populating genres")
    genres = ["პოეზია", "პროზა", "წერილები", "სხვა"]
    for genre in genres:
        Genre(name=genre).create()

    click.echo("Populating languages")
    languages = ["ქართული", "ინგლისური", "რუსული"]
    for language in languages:
        Language(name=language).create()
