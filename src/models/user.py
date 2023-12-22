from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


from src.extensions import db
from src.models.base import BaseModel



class User(BaseModel, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)



  
