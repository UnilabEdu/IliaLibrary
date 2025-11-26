from src.admin.base import SecureModelView
from flask import redirect, url_for
from flask_login import current_user

from wtforms import PasswordField

class UserView(SecureModelView):
    column_list = ["username", "role"]
    form_excluded_columns = ["password"]

    form_extra_fields = {
        "password": PasswordField("Password")
    }

    form_columns = ["username", "password", "role"]

    def on_model_change(self, form, model, is_created):
        if form.password.data:
            model.password = form.password.data

    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == "superadmin"

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))