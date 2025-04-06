from src.extensions import db
from src.models.base import BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

class Book(BaseModel):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    media_type_id = db.Column(db.ForeignKey("media_types.id"), comment="მედიის ტიპი", nullable=False)
    author = db.Column(db.String(), comment="ავტორი")
    title = db.Column(db.String, comment="სახელი", nullable=False)
    page_count = db.Column(db.Integer, comment="გვერდების რაოდენობა")
    language_id = db.Column(db.ForeignKey("languages.id"), comment="ენა", nullable=False)
    publisher = db.Column(db.String(), comment="გამომცემლობა")
    publish_location = db.Column(db.String(), comment="გამოცემის ადგილი")
    publish_year = db.Column(db.Integer(), comment="გამოცემის წელი")
    isbn = db.Column(db.String, unique=True, comment="ISBN")
    issn = db.Column(db.String, unique=True, comment="ISSN")
    journal_name = db.Column(db.String, comment="ჟურნალის სახელწოდება")
    volume_name = db.Column(db.String, comment="კრებულის სახელწოდება")
    id_number = db.Column(db.String, comment="ნომერი")
    edition = db.Column(db.String, comment="გამოცემა")
    genre_id = db.Column(db.ForeignKey("genres.id"), comment="ჟანრი", nullable=False)
    issue_number = db.Column(db.Integer, comment="ტომი")
    liable_person = db.Column(db.String, comment="პასუხისმგებელი პირი")
    liable_organization = db.Column(db.String(), comment="პასუხისმგებელი ორგანიზაცია")
    volume_number = db.Column(db.Integer, comment="სერია")
    copies = db.Column(db.Integer, comment="ტირაჟი")
    physical_description = db.Column(db.String, comment="ფიზიკური აღწერილობა")
    cover_image = db.Column(db.String, nullable=False)
    book_file = db.Column(db.String, nullable=False)
    annotation = db.Column(db.String, comment="ანოტაცია")

    view_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)

    media_type = db.relationship("MediaType", back_populates="books")
    language = db.relationship("Language", back_populates="books")
    genre = db.relationship("Genre", back_populates="books")
    book_content = db.relationship("BookContent", back_populates="books")

    def __repr__(self):
        return self.title


class BookContent(BaseModel):
    __tablename__ = "book_contents"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    page_number = db.Column(db.Integer)
    book_id = db.Column(db.ForeignKey("books.id"))
    books = db.relationship("Book", back_populates="book_content")

    def __repr__(self):
        return self.name


class MediaType(BaseModel):
    __tablename__ = "media_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship("Book", back_populates="media_type")

    def __repr__(self):
        return self.name


class Genre(BaseModel):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship("Book", back_populates="genre")

    def __repr__(self):
        return self.name


class Language(BaseModel):
    __tablename__ = "languages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship("Book", back_populates="language")

    def __repr__(self):
        return self.name