from src.admin.base import SecureModelView


class GenericView(SecureModelView):
    column_labels = {"name": "სახელი"}
