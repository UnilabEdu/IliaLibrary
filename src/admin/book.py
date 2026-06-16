from flask_admin import expose
from flask_admin.contrib.sqla.filters import FilterEqual
from flask_admin.form.upload import ImageUploadField, FileUploadField
from flask_admin.model.form import InlineFormAdmin
from flask_login import current_user
from markupsafe import Markup
from wtforms.fields import TextAreaField

from src.config import Config
from src.admin.utils import ViewRowAction, GenericEqualFilter, _get_filter_options, gen_name
from src.admin.base import SecureModelView
from src.models import BookContent, Book, Genre, MediaType, Language


class InlineBookcontentView(InlineFormAdmin):
    column_labels = {"name": "სათაური", "page_number": "გვერდის ნომერი PDF დოკუმენტის მიხედვით"}


class BookView(SecureModelView):
    page_size = 15
    column_list = ["cover_image", "media_type", "author", "title", "page_count", "language", "publisher", "publish_location",
                   "publish_year", "isbn", "issn", "journal_name", "volume_name", "id_number", "edition", "genre",
                   "issue_number", "liable_person", "liable_organization", "volume_number", "copies",
                   "physical_description", "annotation"]

    column_extra_row_actions = [ViewRowAction("fa fa-eye")]
    column_default_sort = ("created_at", True)
    column_labels = {"media_type": "მედიის ტიპი",
                     "author": "ავტორი",
                     "title": "სათაური",
                     "page_count": "გვერდების რაოდენობა",
                     "language": "ენა",
                     "publisher": "გამომცემლობა",
                     "publish_location": "გამოცემის ადგილი",
                     "publish_year": "გამოცემის წელი",
                     "isbn": "ISBN",
                     "issn": "ISSN",
                     "journal_name": "ჟურნალის სახელწოდება",
                     "volume_name": "კრებულის სახელწოდება",
                     "id_number": "ნომერი",
                     "volume_number": "სერია",
                     "genre": "ჟანრი",
                     "edition": "გამოცემა",
                     "liable_person": "პასუხისმგებელი პირი",
                     "liable_organization": "პასუხისმგებელი ორგანიზაცია",
                     "issue_number": "ტომი",
                     "copies": "ტირაჟი",
                     "physical_description": "ფიზიკური აღწერილობა",
                     "cover_image": "წიგნის ყდა",
                     "book_file": "წიგნის PDF",
                     "annotation": "ანოტაცია",
                     "view_count": "ნახვები",
                     "created_at": "ატვირთვის თარიღი"}
    column_searchable_list = ["author", "title", "isbn", "issn", "journal_name", "volume_name"]
    column_formatters = {"annotation": lambda v,c,m,n: f"{m.annotation[0:50]}..." if len(m.annotation) > 50 else m.annotation,
                         "cover_image": lambda v,c,m,n: Markup(f"<img src=/static/upload/{m.cover_image} style='width: 80px; height: 100px; border-radius: 16px;'/>")}

    form_overrides = {"cover_image": ImageUploadField,
                      "book_file": FileUploadField,
                      "physical_description": TextAreaField,
                      "annotation": TextAreaField}

    form_args = {"cover_image": {"base_path": Config.UPLOAD_PATH, "url_relative_path": "upload/", 'namegen': gen_name},
                 "book_file": {"base_path": Config.UPLOAD_PATH, "label": "pdf-ის ატვირთვა", 'namegen': gen_name}}

    form_columns = ["book_file",] + column_list
    inline_models = [InlineBookcontentView(BookContent)]

    def get_filters(self):
        _dynamic_filters = getattr(self, 'dynamic_filters', None)
        if _dynamic_filters:
            return (super(BookView, self).get_filters() or []) + _dynamic_filters
        else:
            return super(BookView, self).get_filters()
    @expose('/')
    def index_view(self):
        self.dynamic_filters = []
        self.dynamic_filters.extend([
            GenericEqualFilter(column=Book.genre_id, name='ჟანრი', options=_get_filter_options(Genre)),
            GenericEqualFilter(column=Book.language_id, name='ენა', options=_get_filter_options(Language)),
            GenericEqualFilter(column=Book.media_type_id, name='მედიის ტიპი', options=_get_filter_options(MediaType)),
        ])
        self._refresh_filters_cache()
        return super(SecureModelView, self).index_view()

    def is_accessible(self):
        return current_user.is_authenticated

    @property
    def can_delete(self):
        return current_user.role == "superadmin"