from flask import Blueprint, render_template

main_blueprint = Blueprint('main', __name__, template_folder='templates')

@main_blueprint.route('/', methods=['GET', 'POST']) 
def index():
    return render_template('main/index.html') 

@main_blueprint.route('/about-page',methods=['GET'])
def about():
    return render_template('main/about-project.html')

@main_blueprint.route('/book/1', methods=['GET'])
def book():
    return render_template('main/book-details.html')

@main_blueprint.route('/read-book/1', methods=['GET'])
def read_book():
    return render_template('main/flip-page.html')
