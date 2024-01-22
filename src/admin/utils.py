from flask_admin.model.template import BaseListRowAction, LinkRowAction



class ViewRowAction(LinkRowAction):

    def __init__(self, icon_class, url = None):
        super(ViewRowAction, self).__init__(icon_class, url)



    def render(self, context, row_id, row):
        n = self._resolve_symbol(context, 'row_actions.link')
        return n(self, f"/book/{row.id}")