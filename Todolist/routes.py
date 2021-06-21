import os
import secrets
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


# function to save profile picture
def show_picture(pic_data):
    random_hex = secrets.token_hex(8)
    _ , file_ext = os.path.splitext(pic_data.filename)
    picture = random_hex + file_ext
    path = os.path.join(app.root_path,'static','Images',picture)
    pic_data.save(path)
    return picture


@app.route('/profile/', methods = ['GET','POST'])
@login_required
def profile():
    form = Profile()
    if form.validate_on_submit():
        if form.picture.data:
            image = show_picture(form.picture.data)
            current_user.image_file = image
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.user_info = form.userInfo.data
        db.session.commit()
        flash('Your account has been updated','info')
        return redirect(url_for('profile'))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.userInfo.data = current_user.user_info
    image = url_for('static',filename = 'Images/'+current_user.image_file)
    return render_template('profile.html',title = 'Profile', form = form, image = image)


@app.route('/list/', methods = ['GET','POST'])
@login_required
def list():
    
    return render_template('list.html', title = 'Add Items')
