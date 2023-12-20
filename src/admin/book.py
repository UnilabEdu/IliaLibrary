from src.config import Config
from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField


from wtforms.validators import DataRequired
from wtforms.fields import SelectField


class BookView(ModelView):

    form_overrides = {"media_type": SelectField,
                      "cover_image" : ImageUploadField,
                      "volume_name" : SelectField,
                      "topic": SelectField,
                      "publish_location" : SelectField, 
                      "publishers" : SelectField, 
                      "series" : SelectField,
                      "editors" : SelectField,
                      "collections" : SelectField}
    

    form_args = {"media_type": {"choices" : [] },
                  "cover_image" : {"base_path": Config.UPLOAD_PATH},
                  "volume_name" : {"choices" : []},
                  "topic" :  {"choices" : []},
                    }
    
    column_default_sort = "publish_data"