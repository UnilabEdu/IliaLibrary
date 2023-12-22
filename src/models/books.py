from src.extensions import db
from src.models.base import BaseModel
from datetime import datetime

class Book(BaseModel):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    volume_name = db.Column(db.String)
    title = db.Column(db.String)
    media_type = db.Column(db.String)
    cover_image = db.Column(db.String)
    annotation = db.Column(db.String)
    volume_number = db.Column(db.Integer)
    view_count = db.Column(db.Integer)
    edition = db.Column(db.Integer)
    copies = db.Column(db.Integer)
    publish_location = db.Column(db.String)
    publish_year = db.Column(db.Integer)
    editor = db.Column(db.String)
    page_count = db.Column(db.Integer)
    book_height = db.Column(db.Float)
    additional_information = db.Column(db.String)
    book_file = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    publisher_id = db.Column(db.Integer, db.ForeignKey("publisher.id"))
    publisher = db.relationship("Publisher", back_populates="book")
    
    series = db.relationship("Series", back_populates="book", secondary="book_series")

    theme = db.relationship("Theme", back_populates="book", secondary="book_theme")
    collections = db.relationship("Collection", back_populates="book", secondary="book_collection")
    book_content = db.relationship("Bookcontent", back_populates = "book")
    author = db.relationship("Author", back_populates="book", secondary="book_author")

class Author(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    last_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    book_count = db.Column(db.Integer)
    book = db.relationship("Book", back_populates="author", secondary="book_author")


    def __repr__(self):
        return f"{self.name} {self.last_name}"

class BookAuthor(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))


class Series(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    book = db.relationship("Book", back_populates="series", secondary="book_series")
    book_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.name


class BookSeries(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    series_id = db.Column(db.Integer, db.ForeignKey("series.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))


class Theme(BaseModel):
    __tablename__ = 'themes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    book = db.relationship("Book", back_populates="theme", secondary="book_theme")
    book_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.name


class BookTheme(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    theme_id = db.Column(db.Integer, db.ForeignKey("themes.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))


class Bookcontent(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    page_number = db.Column(db.Integer)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    book = db.relationship("Book", back_populates="book_content")


class Publisher(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    book = db.relationship("Book", back_populates="publisher")
    book_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.name



class Collection(BaseModel):
    __tablename__ = 'collections'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    book = db.relationship("Book", back_populates="collections", secondary="book_collection")
    book_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.name


class BookCollection(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    collection_id = db.Column(db.Integer, db.ForeignKey("collections.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))