from src.config import Config
from src.admin.utils import ViewRowAction
from src.admin.base import SecureModelView, SecureIndexView

from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField
from flask_admin.model.template import BaseListRowAction, LinkRowAction



class CollectionView(ModelView):

    form_overrides = {"image" : ImageUploadField}

    form_args = {"image" : {"base_path": Config.UPLOAD_PATH}}

    column_extra_row_actions = [ViewRowAction("fa fa-eye")]

    column_default_sort = ("created_at", True)

    page_size = 15

    column_labels = {"name" : "კოლექციები", "book_count" : "კოლექციაში წიგნების რაოდენობა", "image" : "სურათის დამატება"}

    column_list = ["name", "book_count"]

    column_searchable_list = ["name"]

    form_columns = ["name", "image"]

