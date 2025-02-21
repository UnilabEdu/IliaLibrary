from flask import Blueprint, render_template
from sqlalchemy import or_

from flask import request
from src.models.books import Book
from src.views.main.pagination import paginate_query

main_blueprint = Blueprint('main', __name__, template_folder='templates')


@main_blueprint.route('/', methods=['GET', 'POST']) 
def index():
    page = request.args.get("page", 1, type=int)
    pagination = paginate_query(Book.query, page)
    books = pagination.items
    
# ----------------------
    query = Book.query 
    media_type = request.args.getlist('mediaType')  
    genre = request.args.getlist('genre')  

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

        books = query.all()
        print('media got:', books)
        
    if genre and len(genre)>0:
        print(books)

        refine = {
            "1":"პოეზია",
            "2":"პროზა",
            "3":"წერილები",
            "4":"სხვა"
        }

        conditions = [Book.genre == refine.get(el) for el in genre if refine.get(el)]

        if conditions:
            query = query.filter(or_(*conditions))  

        books = query.all()
        print('genre got:', books)

# ----------------------
    return render_template('main/index.html',books=books, pagination=pagination) 


@main_blueprint.route('/about-page',methods=['GET'])
def about():
    return render_template('main/about-project.html')

@main_blueprint.route('/book/<int:id>', methods=['GET'])
def book(id):
    return render_template('main/book-details.html', id=id)

@main_blueprint.route('/read-book/1', methods=['GET'])
def read_book():
    return render_template('main/flip-page.html')
