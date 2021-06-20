from flask import render_template, Flask, url_for, session

# initializing the application
app = Flask(__name__)



# routes 

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title="Homepage")


@app.route('/register')
def register():
    return render_template('register.html',title="Register")


@app.route('/login')
def login():
    return render_template('login.html',title="Login")

