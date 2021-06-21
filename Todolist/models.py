from datetime import datetime
from Todolist import db

# database tables 
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(60), unique = True, nullable = False)
    image_file = db.Column(db.String, nullable = False, default = 'default.png')
    password = db.Column(db.Integer, nullable = False)
    user_info = db.Column(db.Text, default = 'Hi, I am here.')
    item = db.relationship('Item', backref = 'client', lazy = True)


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(30), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

