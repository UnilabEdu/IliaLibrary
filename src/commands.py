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
    media_types = ["წიგნები", "პერიოდიკა", "წერილები", "ხელნაწერები", "აუდიო", "ფოტო"]
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

    book1 = Book(title="მოთხრობები", media_type_id=1,author='TEST-1', cover_image="diogene.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="2012", page_count=20, language_id=1, genre_id=1,
                 book_file="motxrobebi.pdf",book_content=[BookContent(name="თავი 1", page_number=3),
        BookContent(name="თავი 2", page_number=35),BookContent(name="თავი 1111111111111111111111111111111111111111111111111111111111111111", page_number=12),
        BookContent(name="თავი 8", page_number=4),BookContent(name="თავი 9", page_number=5),BookContent(name="თავი 10", page_number=6),BookContent(name="თავი 3", page_number=7),BookContent(name="თავი 4", page_number=8),BookContent(name="თავი 5", page_number=9),BookContent(name="თავი 6", page_number=13),BookContent(name="თავი 7", page_number=23),])
    book1.create()

    book2 = Book(title="განდეგილი", media_type_id=1, author='TEST-2',cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="2012", page_count=15, language_id=1, genre_id=1,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="თავი 1", page_number=2),
        BookContent(name="თავი 2", page_number=15)])
    book2.create()
    # ---------------TEST-----------
    book3 = Book(title="TEST1", media_type_id=1, cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="1900", page_count=15, language_id=1, genre_id=1,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="თავი 1", page_number=4),
        BookContent(name="adkahdakd", page_number=15)])
    book3.create()

    book4 = Book(title="TEST2", media_type_id=1, cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="2000", page_count=15, language_id=1, genre_id=3,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="TEST2", page_number=10),
        BookContent(name="dfkjls;f", page_number=22)])
    book4.create()
    book5 = Book(title="TEST3", media_type_id=1, cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="1991", page_count=15, language_id=1, genre_id=3,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="TEST5", page_number=10),
        BookContent(name="dfkjls;f", page_number=22)])
    book5.create()
    book6 = Book(title="TEST4", media_type_id=1, cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="1990", page_count=15, language_id=1, genre_id=3,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="TEST6", page_number=10),
        BookContent(name="dfkjls;f", page_number=22)])
    book6.create()
    book7 = Book(title="TEST1", media_type_id=1, cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="1900", page_count=15, language_id=1, genre_id=1,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="თავი 1", page_number=4),
        BookContent(name="adkahdakd", page_number=15)])
    book7.create()

    book8 = Book(title="TEST2", media_type_id=1, cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="2000", page_count=15, language_id=1, genre_id=3,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="TEST2", page_number=10),
        BookContent(name="dfkjls;f", page_number=22)])
    book8.create()
    book9 = Book(title="TEST3", media_type_id=1, cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="1991", page_count=15, language_id=1, genre_id=3,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="TEST5", page_number=10),
        BookContent(name="dfkjls;f", page_number=22)])
    book9.create()
    book10 = Book(title="TEST4", media_type_id=1, cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="1990", page_count=15, language_id=1, genre_id=3,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="TEST6", page_number=10),
        BookContent(name="dfkjls;f", page_number=22)])
    book10.create()
    book11 = Book(title="TEST1", media_type_id=1, cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="1900", page_count=15, language_id=1, genre_id=1,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="თავი 1", page_number=4),
        BookContent(name="adkahdakd", page_number=15)])
    book11.create()

    book12 = Book(title="TEST2", media_type_id=1, cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="2000", page_count=15, language_id=1, genre_id=3,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="TEST2", page_number=10),
        BookContent(name="dfkjls;f", page_number=22)])
    book12.create()
    book13 = Book(title="TEST3", media_type_id=1, cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="1991", page_count=15, language_id=1, genre_id=3,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="TEST51234", page_number=10),
        BookContent(name="dfkjls;f", page_number=22)])
    book13.create()
    book14 = Book(title="TEST4", media_type_id=1, cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="1990", page_count=15, language_id=1, genre_id=3,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="TEST1234", page_number=10),
        BookContent(name="dfkjls;f", page_number=22)])
    book14.create()

