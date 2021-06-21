from os import urandom
from datetime import datetime
from flask import render_template, Flask, url_for, session, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from form import Register, Login


# initializing the application
app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


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




# routes 
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title="Homepage")


@app.route('/register', methods=['GET','POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        flash('You have registerd successfully','info')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)


@app.route('/login',methods=['GET','POST'])
def login():
    form = Login()
    return render_template('login.html', title="Login", form=form)









