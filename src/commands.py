from flask.cli import with_appcontext
import click


from src.models import Book, Series, BookSeries, Theme, BookTheme, Publisher, Collection, BookCollection
from src.extensions import db


def init_db():
    db.drop_all()
    db.create_all()



@click.command("init_db")
@with_appcontext
def init_db_command():
    click.echo("Database creation in porgress")
    init_db()
    click.echo("Database created")