from flask import render_template,  url_for, flash, redirect, request
from flask_login import login_user, logout_user, current_user, login_required
from Todolist import app, db, bcrypt
from Todolist.form import Register, Login, Profile
from Todolist.models import User, Item



# routes 
@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html',title="Homepage")


@app.route('/register/', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Register()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)
        user = User(username = form.username.data, password = hash_pw, email = form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('You have registerd successfully','info')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)


@app.route('/login/',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user, remember = form.remember.data)
            next = request.args.get('next')
            flash('You have logged in successfully','info')
            return redirect(next) if next else redirect(url_for('home'))
        else:
            flash('either email or password doesn\'t match','warning')
    return render_template('login.html', title="Login", form=form)


@app.route('/home/logout/')
def logout():
    logout_user()
    flash('You have logged out successfully','info')
    return redirect(url_for('home'))


@app.route('/profile/',methods = ['GET','POST'])
@login_required
def profile():
    form = Profile()
    return render_template('profile.html',title = 'Profile', form = form)


@app.route('/list/', methods = ['GET','POST'])
@login_required
def list():
    return render_template('list.html', title = 'Add Items')
