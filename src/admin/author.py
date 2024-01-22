from src.config import Config
from src.admin.utils import ViewRowAction
from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField
from flask_admin.model.template import BaseListRowAction, LinkRowAction
   

class AuthorView(ModelView):

    form_overrides = {"image" : ImageUploadField}

    form_args = {"image" : {"base_path": Config.UPLOAD_PATH}}

    column_extra_row_actions = [ViewRowAction("fa fa-eye")]

    column_default_sort = ("created_at", True)

    page_size = 15

    column_labels = {"name" : "სახელი", "last_name" : "გვარი", "book_count" : "წიგნების რაოდენობა", "image" : "სურათის დამატება"}

    column_list = ["name", "last_name", "book_count"]

    column_searchable_list = ["name", "last_name"]

    form_columns = ["name", "last_name", "image"]