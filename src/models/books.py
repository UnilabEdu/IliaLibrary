from src.extensions import db
from src.models.base import BaseModel

class Book(BaseModel):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    media_type = db.Column(db.String)
    cover_image = db.Column(db.String)
    annotation = db.Column(db.String)
    volume_name = db.Column(db.String)
    volume_number = db.Column(db.Integer)
    topic = db.Column(db.String)
    view_count = db.Column(db.Integer)
    edition = db.Column(db.String)
    publish_location = db.Column(db.String)
    publish_date = db.Column(db.String)
    publish_amount = db.Column(db.Float)
    editor = db.Column(db.String)
    page_count = db.Column(db.Integer)
    book_height = db.Column(db.Float)
    additional_information = db.Column(db.String)
    book_file = db.Column(db.String)

    series = db.relationship("Series", back_populates="book", secondary="book_series")
    theme = db.relationship("Theme", back_populates="book", secondary="book_theme")
    publishers = db.relationship("Publisher", back_populates="book", secondary="book_publisher")
    collections = db.relationship("Collection", back_populates="book", secondary="book_collection")


class Series(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    book = db.relationship("Book", back_populates="series", secondary="book_series")


class BookSeries(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    series_id = db.Column(db.Integer, db.ForeignKey("series.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))


class Theme(BaseModel):
    __tablename__ = 'themes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    book = db.relationship("Book", back_populates="theme", secondary="book_theme")


class BookTheme(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    theme_id = db.Column(db.Integer, db.ForeignKey("themes.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))


class BookContent(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    page_number = db.Column(db.Integer)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))


class Publisher(BaseModel):
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    book = db.relationship("Book", back_populates="publishers", secondary="book_publisher")


class BookPublisher(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    publisher_id = db.Column(db.Integer, db.ForeignKey("publishers.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))


class Collection(BaseModel):
    __tablename__ = 'collections'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    book = db.relationship("Book", back_populates="collections", secondary="book_collection")


class BookCollection(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    collection_id = db.Column(db.Integer, db.ForeignKey("collections.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))