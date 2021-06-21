from os import urandom
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# initializing the application
app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


from Todolist import routes