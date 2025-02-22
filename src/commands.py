from flask.cli import with_appcontext
import click


from src.models import User, Book, Author,  Series, BookSeries, Theme, BookTheme, Publisher, Collection, BookCollection, PublishLocation
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



@click.command("populate_db")
@with_appcontext
def populate_db_command():
    click.echo("populating db")
    user1 = User(username="admin", password="admin123")
    user1.password = "admin123" 
    user2 = User(username="admin2", password="admin456")
    user1.create()
    user2.create()

    click.echo("populate book")
    book1 = Book(title="განდეგილი", media_type="წიგნი", cover_image =  "gandegili.jpg", annotation =  "ილია ჭავჭავაძის მოთხრობები", edition =  "1", copies = "62445", 
                       publish_year = "2022",  page_count = "284", book_height = "15.5", additional_information =  "დამატებითი ტექსტური ინფორმაცია", 
                      book_file = "motxrobebi.pdf", language = "ქართული")
    book1.create()

    # for test #############################
    book2 = Book(title="123", genre="პოეზია", media_type="წერილები", cover_image =  "motxrobebi.jpg", annotation =  "ილია ჭავჭავაძის მოთხრობები", edition =  "1", copies = "62445", 
                    publish_year = "2002",  page_count = "284", book_height = "15.5", additional_information =  "დამატებითი ტექსტური ინფორმაცია", 
                    book_file = "motxrobebi.pdf", language = "ქართული")
    book2.create()
    
    book3 = Book(title="qwerty", genre="პროზა", media_type="პერიოდიკა", cover_image =  "motxrobebi.jpg", annotation =  "ილია ჭავჭავაძის მოთხრობები", edition =  "1", copies = "62445", 
                    publish_year = "2015",  page_count = "284", book_height = "15.5", additional_information =  "დამატებითი ტექსტური ინფორმაცია", 
                    book_file = "motxrobebi.pdf", language = "რუსული")
    book3.create()
    
    book4 = Book(title="მოთხრობები", genre="წერილები", media_type="ხელნაწერები", cover_image =  "motxrobebi.jpg", annotation =  "ილია ჭავჭავაძის მოთხრობები", edition =  "1", copies = "62445", 
                    publish_year = "2015",  page_count = "284", book_height = "15.5", additional_information =  "დამატებითი ტექსტური ინფორმაცია", 
                    book_file = "motxrobebi.pdf", language = "ქართული")
    book4.create()  

    book5 = Book(title="მოთხრობები", genre="სხვა", media_type="აუდიო", cover_image =  "motxrobebi.jpg", annotation =  "ილია ჭავჭავაძის მოთხრობები", edition =  "1", copies = "62445", 
                    publish_year = "2012",  page_count = "284", book_height = "15.5", additional_information =  "დამატებითი ტექსტური ინფორმაცია", 
                    book_file = "motxrobebi.pdf", language = "ინგლისური")
    book5.create()  

    book6 = Book(title="მოთხრობები", genre="პოეზია", media_type="ფოტო", cover_image =  "motxrobebi.jpg", annotation =  "ილია ჭავჭავაძის მოთხრობები", edition =  "1", copies = "62445", 
                    publish_year = "2012",  page_count = "284", book_height = "15.5", additional_information =  "დამატებითი ტექსტური ინფორმაცია", 
                    book_file = "motxrobebi.pdf", language = "ქართული")
    book6.create()
    ########################################

    click.echo("populate editor")
    editor1 = Author(name = "სერგეი", last_name =  "მესხი")
    editor1.create()

    click.echo("populate series")
    series1 = Series(name = "50 წიგნი", image = "50_wigni.jpg")
    series2 = Series(name = "კიდევ 49 წიგნი", image = "49_wigni.jpg")
    series1.create()
    series2.create()

    click.echo("populate publisher")
    publisher1 = Publisher(name = "დიოგენე", image = "diogene.jpg")
    publisher2 = Publisher(name = "პალიტრა L", image = "palitra.png")
    publisher1.create()
    publisher2.create()

    click.echo("populate publish location")
    location1 = PublishLocation(location = "თბილისი")
    location2 = PublishLocation(location = "ქუთაისი")
    location1.create()
    location2.create()

    click.echo("populate collections")
    collection1 = Collection(name = "ილიაუნის ბიბლიოთეკა")
    collection1.create()