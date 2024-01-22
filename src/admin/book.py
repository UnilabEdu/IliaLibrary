from src.config import Config
from src.admin.utils import ViewRowAction
from src.admin.base import SecureModelView, SecureIndexView
from src.models import Bookcontent

from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField, FileUploadField
from flask_admin.model.form import InlineFormAdmin
from flask_admin.form import rules
from flask_admin.model.form import InlineFormAdmin
from wtforms import StringField, IntegerField
from flask_admin.model.template import BaseListRowAction, LinkRowAction
from wtforms.validators import DataRequired
from wtforms.fields import SelectField



class InlineBookcontentView(InlineFormAdmin):

    column_labels = {"name" : "სათაური", "page_number" : "გვერდის ნომერი pdf დოკუმენტის მიხედვით"}


class BookView(ModelView):

    form_overrides = {"cover_image" : ImageUploadField,
                      "book_file" : FileUploadField, 
                      "media_type" : SelectField}

    form_args = {"cover_image" : {"base_path": Config.UPLOAD_PATH},
                 "book_file" : {"base_path" : Config.UPLOAD_PATH, "label" : "ფაილის ატვირთვა"},
                 "media_type" : {"choices" : [("book", "წიგნი")]}
                    }
    
    column_extra_row_actions = [ViewRowAction("fa fa-eye")]
    
    column_default_sort = ("created_at", True)

    page_size = 15

    column_sortable_list = ["volume_name", "title", "publish_year", "book_file", "view_count", "created_at", ("theme", "theme.name"), ("series", "series.name"), ("publisher", "publisher.name"),]

    column_labels = {"title": "სათაური", "media_type": "მედიის ტიპი", "cover_image": "წიგნის ყდის ფოტო", "annotation": "ანოტაცია", "volume_name": "ტომის სახელი", "volume_number": "ტომის ნომერი", "view_count": "ნახვების რაოდენობა", "edition": "გამოცემა", "copies" : "ტირაჟი", 
                      "publish_location": "გამოცემის ადგილი", "publish_year": "გამოცემის წელი", "editor": "რედაქტორები", "page_count": "გვერდების რაოდენობა", "book_height": "სიმაღლე სმ-ებში", "additional_information": "დამატებითი ტექსტური ინფორმაცია", 
                      "book_file": "pdf-ის ლინკი", "created_at": "დამატების თარიღი", "publisher" : "გამომცემლობის სახელი", "collections" : "კოლექციები", "series" : "სერიის/ების სახელი", "theme" : "თემატიკის/ების სახელი", "book_content" : "სარჩევი", "author" : "სახელი და გვარი"}

    column_exclude_list = ["id", "media_type", "cover_image", "annotation", "volume_number", "topic", "edition", "publish_location", "publish_amount", "editor", "page_count", "book_height", "additional_information"]

    column_list = ["volume_name", "title", "theme", "series",  "publisher", "publish_year", "book_file", "view_count", "created_at"]

    form_columns = ["book_file", "media_type", "title", "cover_image", "annotation", "theme",  "volume_name", "volume_number", "series", "book_content", "edition", "publish_location", "publisher", "publish_year", "copies", "editor", "author", "page_count", "book_height", "additional_information", "collections" ]


    column_searchable_list = ["volume_name", "title",  "publish_year", "publisher.name", "theme.name", "series.name", "book_file", "view_count", "created_at"]

    inline_models = [InlineBookcontentView(Bookcontent, )]


    