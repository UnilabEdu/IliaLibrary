from flask import Blueprint, render_template

home_blueprint = Blueprint('main', __name__, template_folder='../../templates')

@home_blueprint.route('/', methods=['GET', 'POST']) 
def index():
    return render_template('home/index.html') 
