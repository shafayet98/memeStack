from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from mainproject.models import User


class LoginForm(FlaskForm):
    email = StringField("Enter Email",validators=[DataRequired(),Email()])
    password =  PasswordField("Enter password",validators=[DataRequired()])
    submit = SubmitField("Sign In")

class RegistrationForm(FlaskForm):
    email = StringField("Enter Email",validators = [DataRequired(),Email()])
    username = StringField("Enter Username",validators= [DataRequired()])
    password = PasswordField("Enter Password",validators= [DataRequired(),EqualTo('password_confirm',message="password dosn't match")])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Signup")

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered")
    
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username Taken")

class UpdateUserForm(FlaskForm):
    email = StringField("Email",validators = [DataRequired(),Email()])
    username = StringField("Username",validators= [DataRequired()])
    picture = FileField("Update Profile Pictures", validators= [FileAllowed(['jpg','jpeg','png'])])
    submit = SubmitField("Update")

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Updated Email already registered")
    
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Updated Username as already taken")

