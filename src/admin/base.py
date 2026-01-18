from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, expose
from flask_login import current_user, logout_user


class SecureModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login'))


class SecureIndexView(AdminIndexView):
    def is_visible(self):
        return False

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login'))


    @expose('/')
    def index(self):
        return redirect(url_for('book.index_view'))

    @expose('/logout/')
    def logout(self):
        logout_user()
        return redirect(url_for('auth.login'))