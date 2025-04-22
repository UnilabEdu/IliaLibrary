from flask import has_request_context
from flask_admin.contrib.sqla.filters import FilterEqual
from flask_admin.model.template import BaseListRowAction, LinkRowAction
from flask_admin.model import filters

from src.models import Genre


class ViewRowAction(LinkRowAction):

    def __init__(self, icon_class, url=None):
        super(ViewRowAction, self).__init__(icon_class, url)

    def render(self, context, row_id, row):
        n = self._resolve_symbol(context, 'row_actions.link')
        return n(self, f"/book/{row.id}")


class GenericEqualFilter(FilterEqual):
    def apply(self, query, value, alias=None):
        return query.filter(self.get_column(alias) == value)

    def operation(self):
        return "არის"

def _get_filter_options(cls):
    return [(model.id, model.name) for model in cls.query.all()]