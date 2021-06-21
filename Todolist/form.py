from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import EqualTo, Email, Length, InputRequired, ValidationError
from Todolist.models import User



# class to create register and login form fields
class Register(FlaskForm):
    username = StringField(label = 'Username', validators=[InputRequired(), 
                            Length(min=5,max=50,message="username should contain atleast 5 characters")])
    email = StringField(label = "Email", validators=[InputRequired(), 
                        Length(min=13,max=60,message="email should contain atleast 13 characters"),
                        Email(message = "email address is not valid")])
    password = PasswordField(label = "Password", validators=[InputRequired(), 
                            Length(min=8,max=50,message="password should contain atleast 8 characters")])
    reenter__password = PasswordField(label = "Re-enter password", validators=[InputRequired(),
                                    EqualTo('password', message="must match with password")])
    register = SubmitField('Register')

    # custom validators 
    def validate_username(self,username):
        invalidChar = '!@#$%^&*()+_=`~?><,./"\'\\:;}]{[|'
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('username is already taken, try different username')
        for char in username.data:
            if char in invalidChar:
                raise ValidationError('Username is invalid')

    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('user with this email is already registered, try different email')

    def validate_password(self,password):
        specialChar = '!@#$%^&*()+_=`~?><,./"\'\\:;}]{[|'
        tracker = 0
        for char in password.data:
            if char in specialChar:
                tracker += 1
        if tracker == 0:
            raise ValidationError('password should contain atleast one special character')



class Login(FlaskForm):
    email = StringField(label = "Email", validators=[InputRequired(), 
                        Length(min=13,max=60,message="email should contain atleast 13 characters"),
                        Email(message = "email is not valid")])
    password = PasswordField(label = "Password", validators=[InputRequired(), 
                            Length(min=8,max=50,message="password should contain atleast 8 characters")])
    remember = BooleanField(label = "Remember me")
    login = SubmitField('Login')




class Profile(FlaskForm):
    username = StringField(label = 'Username', validators=[InputRequired(), 
                            Length(min=5,max=50,message="username should contain atleast 5 characters")])
    email = StringField(label = "Email", validators=[InputRequired(), 
                        Length(min=13,max=60,message="email should contain atleast 13 characters"),
                        Email(message = "email address is not valid")])
    userInfo = TextAreaField(label = "About yourself", validators = [InputRequired(), Length(max = 1000, message = "maximum 1000 characters are allowed")])
    update = SubmitField('Update')

    # custom validators 
    def validate_username(self,username):
        invalidChar = '!@#$%^&*()+_=`~?><,./"\'\\:;}]{[|'
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('username is already taken, try different username')
        for char in username.data:
            if char in invalidChar:
                raise ValidationError('Username is invalid')

    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('user with this email is already registered, try different email')

