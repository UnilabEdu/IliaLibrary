from flask import render_template, url_for, redirect, Blueprint
from flask_login import login_user

from src.views.auth.forms import LoginForm
from src.models import User

from uuid import uuid4


auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
        else:
            return render_template('auth/login.html', form=form, error='Invalid username or password')

        print(form.password.data)
        return redirect(url_for('admin.index'))
    return render_template('auth/login.html', form=form)
