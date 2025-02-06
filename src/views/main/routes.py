from flask import Blueprint, render_template

main_blueprint = Blueprint('main', __name__, template_folder='templates')

@main_blueprint.route('/', methods=['GET', 'POST']) 
def index():
    return render_template('home/index.html') 
