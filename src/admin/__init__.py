from flask_admin import Admin
from src.admin.book import BookView
from src.admin.author import AuthorView
from src.admin.publishers import PublisherView
from src.admin.series import SeriesView
from src.admin.theme import ThemeView
from src.admin.collection import CollectionView
from src.admin.base import SecureIndexView
from src.admin.publish_location import PublishLocationView



admin = Admin(index_view=SecureIndexView(), template_mode="bootstrap4")