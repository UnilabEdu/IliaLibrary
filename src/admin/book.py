from src.config import Config
from src.admin.utils import ViewRowAction
from src.admin.base import SecureModelView, SecureIndexView
from src.models import BookContent

from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField, FileUploadField
from flask_admin.model.form import InlineFormAdmin
from wtforms.fields import SelectField


class InlineBookcontentView(InlineFormAdmin):
    column_labels = {"name": "სათაური", "page_number": "გვერდის ნომერი pdf დოკუმენტის მიხედვით"}


class BookView(ModelView):
    form_overrides = {"cover_image": ImageUploadField,
                      "book_file": FileUploadField}

    form_args = {"cover_image": {"base_path": Config.UPLOAD_PATH, "url_relative_path": "upload/"},
                 "book_file": {"base_path": Config.UPLOAD_PATH, "label": "pdf-ის ატვირთვა"}
                }

    column_extra_row_actions = [ViewRowAction("fa fa-eye")]
    column_default_sort = ("created_at", True)
    page_size = 15


