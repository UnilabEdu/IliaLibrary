from src.extensions import db
from src.models.base import BaseModel
from datetime import datetime


class Book(BaseModel):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    media_type_id = db.Column(db.ForeignKey("media_types.id"))
    author = db.Column(db.String())
    title = db.Column(db.String)
    page_count = db.Column(db.Integer)
    language_id = db.Column(db.ForeignKey("languages.id"))
    publisher = db.Column(db.String())
    publish_location = db.Column(db.String())
    publish_year = db.Column(db.Integer())
    isbn = db.Column(db.String, unique=True)
    issn = db.Column(db.String, unique=True)
    journal_name = db.Column(db.String)
    volume_name = db.Column(db.String)
    id_number = db.Column(db.String)
    edition = db.Column(db.String)
    genre_id = db.Column(db.ForeignKey("genres.id"))
    issue_number = db.Column(db.Integer)
    liable_person = db.Column(db.String)
    liable_organization = db.Column(db.String())
    volume_number = db.Column(db.Integer)
    copies = db.Column(db.Integer)
    physical_description = db.Column(db.String)
    cover_image = db.Column(db.String)
    book_file = db.Column(db.String)
    annotation = db.Column(db.String)

    view_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now)

    media_type = db.relationship("MediaType", back_populates="books")
    language = db.relationship("Language", back_populates="books")
    genre = db.relationship("Genre", back_populates="books")
    book_content = db.relationship("BookContent", back_populates="books")


class BookContent(BaseModel):
    __tablename__ = "book_contents"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    page_number = db.Column(db.Integer)
    book_id = db.Column(db.ForeignKey("books.id"))
    books = db.relationship("Book", back_populates="book_content")


class MediaType(BaseModel):
    __tablename__ = "media_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship("Book", back_populates="media_type")


class Genre(BaseModel):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship("Book", back_populates="genre")


class Language(BaseModel):
    __tablename__ = "languages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship("Book", back_populates="language")
