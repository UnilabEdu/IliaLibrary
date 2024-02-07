from src.config import Config
from src.admin.utils import ViewRowAction
from src.admin.base import SecureModelView, SecureIndexView

from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField


       

class ThemeView(ModelView):

    column_formatters = dict(price=lambda Book, c, m, p: m.get_book_count())

    form_overrides = {"image" : ImageUploadField}

    form_args = {"image" : {"base_path": Config.UPLOAD_PATH, "url_relative_path": "upload/"}}

    column_formatters = {"book_count" : lambda v, c, m, p: len(m.book)}

    column_extra_row_actions = [ViewRowAction("fa fa-eye")]

    column_default_sort = ("created_at", True)

    page_size = 15

    column_labels = {"name" : "თემატიკა", "book_count" : "წიგნების რაოდენობა ამ მახასიათებლით", "image" : "სურათის დამატება"}

    column_list = ["name", "book_count"]

    column_searchable_list = ["name"]

    form_columns = ["name", "image"]