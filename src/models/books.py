from src.extensions import db
from src.models.base import BaseModel

class Book(BaseModel):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True)
    part_name = db.Column(db.String)
    title = db.Column(db.String)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    genres = db.relationship('Genre',  back_populates='books')
    
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'))
    series = db.relationship('Series',  back_populates='books')

    publisher_id  =  db.Column(db.Integer, db.ForeignKey('publisher.id'))
    publisher = db.relationship('Publisher',  back_populates='books')
    
    publication_date = db.Column(db.Integer)
    pdf_link = db.Column(db.String)
    user_number =  db.Column(db.Integer)
    add_date = db.Column(db.Integer)

class Genre(BaseModel):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    books = db.relationship('Book',  back_populates='genres')

class Publisher(BaseModel):
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    books = db.relationship('Book', back_populates='publisher')


class Publisher(BaseModel):
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    books = db.relationship('Book', back_populates='publisher')







