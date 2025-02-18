from flask import Blueprint, render_template

main_blueprint = Blueprint('main', __name__, template_folder='templates')

from flask import request
from src.models.books import Book
from src.views.main.pagination import paginate_query



@main_blueprint.route('/', methods=['GET', 'POST']) 
def index():
    page = request.args.get("page", 1, type=int)
    pagination = paginate_query(Book.query, page)
    
    return render_template('main/index.html',books=pagination.items, pagination=pagination) 

@main_blueprint.route('/about-page',methods=['GET'])
def about():
    return render_template('main/about-project.html')

@main_blueprint.route('/book/1', methods=['GET'])
def book():
    return render_template('main/book-details.html')

@main_blueprint.route('/read-book/1', methods=['GET'])
def read_book():
    return render_template('main/flip-page.html')
