from flask_admin import Admin
from src.admin.book import BookView
from src.admin.base import SecureIndexView

admin = Admin(index_view=SecureIndexView(), template_mode="bootstrap4", base_template="admin/admin_base.html")