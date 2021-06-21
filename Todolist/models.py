from datetime import datetime
from Todolist import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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

    def __repr__(self):
        return f'User({self.username},{self.email},{self.user_info})'

    # attributes to work with flask_login package
    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return False
    def is_active(self):
        return True
    def get_id(self):
        return self.id



class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(30), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    def __repr__(self):
        return f'Post({self.item_name} {self.date_posted})'