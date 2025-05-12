from flask.cli import with_appcontext
import click

from src.models import User, Book, MediaType, Language, Genre, BookContent
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

    book1 = Book(title="მოთხრობები", media_type_id=1, cover_image="diogene.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="2012", page_count=20, language_id=1, genre_id=1,
                 book_file="motxrobebi.pdf",book_content=[BookContent(name="თავი 1", page_number=3),
        BookContent(name="თავი 2", page_number=35)])
    book1.create()

    # for test #############################
    book2 = Book(title="განდეგილი", media_type_id=1, cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="2012", page_count=15, language_id=1, genre_id=1,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="თავი 1", page_number=2),
        BookContent(name="თავი 2", page_number=15)])
    book2.create()
