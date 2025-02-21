from flask_sqlalchemy import pagination

def paginate_query(query, page, per_page=16):
    return query.paginate(page=page, per_page=per_page, error_out=False)
