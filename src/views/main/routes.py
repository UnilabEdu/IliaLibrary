from flask import Blueprint, render_template, url_for, session
from sqlalchemy import or_, func

from flask import request
from src.models import Book, MediaType, Language, Genre

main_blueprint = Blueprint('main', __name__, template_folder='templates')


@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get("page", 1, type=int)

    query = Book.query
    search_text = request.args.get('searchQuery')
    media_types = request.args.getlist('mediaType')
    genres = request.args.getlist('genre')
    languages = request.args.getlist('language')
    date_from = request.args.get('dateFrom')
    date_to = request.args.get('dateTo')
    sort_by = request.args.get("sortedBy")

    if media_types and len(media_types) > 0:
        conditions = [Book.media_type_id == media_type_id for media_type_id in media_types]
        if conditions:
            query = query.filter(or_(*conditions))

    if genres and len(genres) > 0:
        conditions = [Book.genre_id == genre_id for genre_id in genres]
        if conditions:
            query = query.filter(or_(*conditions))

    if languages and len(languages) > 0:
        conditions = [Book.language_id == language_id for language_id in languages]
        if conditions:
            query = query.filter(or_(*conditions))

    if date_from and date_to:
        conditions = [Book.publish_year >= date_from[:4], Book.publish_year <= date_to[:4]]
        query = query.filter(*conditions)

    if search_text is not None:
        query = query.filter(or_(Book.title.ilike(f"%{search_text}%")))

    if sort_by is not None:
        if sort_by == 'name-asc':
            query = query.order_by(Book.title.asc())
        elif sort_by == 'name-desc':
            query = query.order_by(Book.title.desc())
        elif sort_by == "year-asc":
            query = query.order_by(Book.publish_year.asc())
        elif sort_by == "year-desc":
            query = query.order_by(Book.publish_year.desc())

    books = query.paginate(page=page, per_page=16, error_out=False)
    return render_template('main/index.html', books=books,
                           genres=Genre.query.all(), media_types=MediaType.query.all(), languages=Language.query.all(), search_text=search_text)


@main_blueprint.route('/about', methods=['GET'])
def about():
    return render_template('main/about-project.html')


@main_blueprint.route('/book/<int:id>', methods=['GET'])
def view_book(id):
    book = Book.query.get(id)
    other_books = Book.query.order_by(func.random()).limit(5).all()

    if 'viewed_book_ids' not in session:
        session['viewed_book_ids'] = list()

    if id not in session['viewed_book_ids']:
        session['viewed_book_ids'].append(id)
        book.view_count += 1
        book.save()

    return render_template('main/book-details.html', book=book, other_books=other_books)


@main_blueprint.route('/read_book/<int:id>', methods=['GET'])
def read_book(id):
    book = Book.query.get(id)
    return render_template('main/flip-page.html', book=book)
