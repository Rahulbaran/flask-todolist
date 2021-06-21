from flask import render_template,  url_for, flash, redirect
from Todolist import app, db
from Todolist.form import Register, Login



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
