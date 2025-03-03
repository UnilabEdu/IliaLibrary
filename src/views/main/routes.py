from flask import Blueprint, render_template, url_for
from sqlalchemy import or_

from flask import request
from src.models.books import Book

main_blueprint = Blueprint('main', __name__, template_folder='templates')


@main_blueprint.route('/', methods=['GET', 'POST']) 
def index():
    page = request.args.get("page", 1, type=int)
    
# ----------------------
    query = Book.query 
    search_text = request.args.get('searchQuery')
    media_type = request.args.getlist('mediaType')  
    genre = request.args.getlist('genre') 
    language = request.args.getlist('language')  
    date_from = request.args.get('dateFrom')  
    date_to = request.args.get('dateTo')  

    if media_type and len(media_type) > 0:
        refine = {
            "1": 'წიგნი',
            "2": 'პერიოდიკა',
            "3": 'წერილები',
            "4": 'ხელნაწერები',
            "5": 'აუდიო',
            "6": 'ფოტო'
        }

        conditions = [Book.media_type == refine.get(el) for el in media_type if refine.get(el)]

        if conditions:
            query = query.filter(or_(*conditions))  

    if genre and len(genre)>0:
        refine = {
            "1":"პოეზია",
            "2":"პროზა",
            "3":"წერილები",
            "4":"სხვა"
        }

        conditions = [Book.genre == refine.get(el) for el in genre if refine.get(el)]

        if conditions:
            query = query.filter(or_(*conditions))  

    if language and len(language)>0:
        refine = {
            "1":"ქართული",
            "2":"ინგლისური",
            "3":"რუსული",
        }

        conditions = [Book.language == refine.get(el) for el in language if refine.get(el)]

        if conditions:
            query = query.filter(or_(*conditions))  

    if date_from and date_to :
        conditions = [Book.publish_year >= date_from[:4], Book.publish_year <= date_to[:4]]
        query = query.filter(*conditions)

    if search_text is not None:
        query = query.filter(or_(Book.title.ilike(f"%{search_text}%"),
        Book.genre.ilike(f"%{search_text}%"),
        Book.media_type.ilike(f"%{search_text}%"),
        Book.language.ilike(f"%{search_text}%")))
# ----------------------

    books = query.paginate(page=page, per_page=16, error_out=False)
    return render_template('main/index.html',books=books) 


@main_blueprint.route('/about-page',methods=['GET'])
def about():
    return render_template('main/about-project.html')

@main_blueprint.route('/book/<int:id>', methods=['GET'])
def book(id):
    book = Book.query.get(id)
    return render_template('main/book-details.html', id=id, book=book)

@main_blueprint.route('/read-book/<int:id>', methods=['GET'])
def read_book(id):
    book = Book.query.get(id)

    return render_template('main/flip-page.html', id=id, book=book)
