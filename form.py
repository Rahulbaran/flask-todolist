from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import EqualTo, Email, Length, InputRequired


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


class Login(FlaskForm):
    email = StringField(label = "Email", validators=[InputRequired(), 
                        Length(min=13,max=60,message="email should contain atleast 13 characters"),
                        Email(message = "email is not valid")])
    password = PasswordField(label = "Password", validators=[InputRequired(), 
                            Length(min=8,max=50,message="password should contain atleast 8 characters")])
    remember = BooleanField(label = "Remember me")
    login = SubmitField('Login')