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
    user1 = User(username="admin", password="admin123", role="admin")
    user1.password = "admin123"
    user1.create()


    user1 = User(username="superadmin", password="superadmin123", role="superadmin")
    user1.password = "superadmin123"
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
                 book_file="motxrobebi.pdf",book_content=[BookContent(name="თავი 1 (3)", page_number=3),
        BookContent(name="თავი 2 (35)", page_number=35),BookContent(name="(12) თავი 1111111111111111111111111111111111111111111111111111111111111111", page_number=12),
        BookContent(name="თავი 3 (4)", page_number=4),BookContent(name="თავი 4 (5)", page_number=5),BookContent(name="თავი 5 (6)", page_number=6),BookContent(name="თავი 6 (7)", page_number=7),BookContent(name="თავი 7 (8)", page_number=8),BookContent(name="თავი 8 (9)", page_number=9),BookContent(name="თავი 9 (13)", page_number=13),BookContent(name="თავი 10 (23)", page_number=23),
        BookContent(name="(24) თავი 123 123 1234567 75353535 111111111111111111111111111111111111111111111111111111111111111", page_number=24),])
    book1.create()

    book2 = Book(title="განდეგილი", media_type_id=1, author='TEST-2',cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="2012", page_count=15, language_id=1, genre_id=1,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="თავი 1", page_number=2),
        BookContent(name="თავი 2", page_number=15)])
    book2.create()
    # ---------------TEST-----------
    book3 = Book(title="თხზულებანი. სრული კრებული ხუთ ტომად. ტ. 3: საქართველოს მატიანე. ცხოვრება და კანონი. წერილები უცხოეთზე", media_type_id=1, cover_image="gandegili.jpg",
                 annotation="ილია ჭავჭავაძის მოთხრობები", edition="1", copies="62445",
                 publish_year="1900", page_count=15, language_id=1, genre_id=1,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="თავი 1", page_number=4),
        BookContent(name="adkahdakd", page_number=15)])
    book3.create()

    book4 = Book(title="თხზულებანი. სრული კრებული ხუთ ტომად. ტ. 3: საქართველოს მატიანე. ცხოვრება და კანონი. წერილები უცხოეთზე თხზულებანი. სრული კრებული ხუთ ტომად. ტ. 3: საქართველოს მატიანე. ცხოვრება და კანონი. წერილები უცხოეთზე ", media_type_id=1, cover_image="gandegili.jpg",
                 annotation="პოემა „განდეგილი“ ილია ჭავჭავაძის შემოქმედების გვიანდელ, ფილოსოფიური ძიებების პერიოდს განეკუთვნება. ილიამ მისი წერა დაარულა 1883 წლის 6 თებერვალს. პოემა საზოგადოებას თავად ავტორმა წაუკითხა იმავე წლის 10 თებერვალს, დავით სარაჯიშვილის სახლში. პირველი პუბლიკაცია 1883 წლის მარტის დასაწყისში ჟურნალ „ივერიის“ მეორე ნომერში შედგა. იმავე წელს ის ცალკე წიგნადაც გამოიცა. პოემა, რომლის მოქმედებაც მყინვარწვერზე ვითარდება, ილიას ერთ-ერთი ყველაზე ღრმა ფილოსოფიური და ალეგორიული ნაწარმოებია. მასში დასმულია სულისა და ხორცის, ზესთამიწიერისა და მიწიერი ცხოვრების მარადიული კონფლიქტი, ასევე ასკეტიზმისა და ადამიანური ვნების დაპირისპირება. პოემის მხატვრული ლოგიკით დაგმობილია ქვეყნიერებისაგან და საზოგადოებრივი ცხოვრებისაგან განდგომა. ილია, მართალია, ავლენს ღრმა ინტერესს რელიგიური მოტივებისადმი, თუმცა საბოლოო ჯამში, უპირატესობას ანიჭებს მიწიერ მოვალეობასა და აქტიურ საზოგადოებრივ მოღვაწეობას, რითაც პოემა ინარჩუნებს მწერლის ეროვნულ-პატრიოტული იდეოლოგიის ერთგულებას. პოემა მდიდარია რომანტიკული ელემენტებით, განსაკუთრებით კი მწყემსი ქალის იდეალიზებული სახით. ნაწარმოების გამოცემას მყისიერი და დიამეტრულად საპირისპირო გამოხმაურება მოჰყვა, რაც მის მწვავე საზოგადოებრივ-პოლიტიკურ მნიშვნელობაზე მიუთითებს. პოზიტიურ შეფასებებთან ერთად, კრიტიკოსთა ნაწილი მას აფასებდა როგორც ფორმით, ისე შინაარსით დაწუნებულს, ზოგიერთი კი მასში ხედავდა ილიას „პესიმისტურ შეხედულებას სააქაოზე“. საქართველოში საბჭოთა რეჟიმის დამყარების და ქართულ ლიტერატურაზე იდეოლოგიური ზეწოლის გაძლიერების პერიოდში ილია ჭავჭავაძის მემკვიდრეობა აქტიურად განიხილებოდა საბჭოთა ლიტერატურათმცოდმეების მიერ. ამ პერიოდში დაიწყო ილიას თხზულებათა კრებულების სისტემატიზებული გამოცემები. 1925 წლის გამოცემა (როგორც 1925-1951 წლების გამოცემების ციკლის ნაწილი), რომელიც 3 ათასიანი ტირაჟით გამოვიდა „უნივერსალური სახალხო ბიბლიოთეკის“ სერიით, ეყრდნობოდა 1892 წლის გამოცემას, რომელიც ტექსტოლოგების მიერ მიჩნეული იყო ილიას ავტორისეული ნების ამსახველ ტექსტად. ამრიგად, „განდეგილის“ 1925 წლის გამოცემა არ არის უბრალოდ ხელახალი ბეჭდვა; ის არის მნიშვნელოვანი რგოლი ილიას კანონიკური ტექსტის დადგენის პროცესში და წარმოადგენს იმ გამოცემების სერიას, რომლითაც საბჭოთა ლიტერატურათმცოდნეობა ცდილობდა ილიას თხზულებების საბოლოო, გასწორებული ვარიანტის შექმნას, 1892 წლის ავტორისეულ წყაროზე დაყრდნობით.", edition="1", copies="62445",
                 publish_year="2000", page_count=15, language_id=1, genre_id=3,
                 book_file="gandegili-1957.pdf",book_content=[BookContent(name="პრეზიდენტისა და მთავრობის შეცვლა საფრანგეთში და მისი საზოგადოებრივი მიზეზები", page_number=10),BookContent(name="ისევ და ისევ ბ-ნ ჟორდანიას უმეცრობანი და მისი წაჯეგ-უკუჯეგობანი", page_number=22),BookContent(name="ცენზურის მიერ შემოკლებული ტექსტი შინაური მიმოხილვისა", page_number=22),BookContent(name="საზოგადოებრივი ცხოვრების ნაკლნი და მისი ეკონომიური მიზეზები (1897)", page_number=22)])
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
    book7 = Book(title="თხზულებანი. სრული კრებული ხუთ ტომად. ტ. 3: საქართველოს მატიანე. ცხოვრება და კანონი. წერილები უცხოეთზე", media_type_id=1, cover_image="gandegili.jpg",
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

