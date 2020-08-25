from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError, Email
import models as mds
from passlib.hash import pbkdf2_sha256


def invalid_credentials(form, field):
    """username and password checker"""
    email_entered = form.email.data
    password_entered = field.data

    user_object = mds.User.query.filter_by(email=email_entered).first()
    if user_object is None:
        raise ValidationError("Email or password incorrect")
    elif not pbkdf2_sha256.verify(password_entered, user_object.password):
        raise ValidationError("Email of password incorrect")

class RegistrationForm(FlaskForm):
    """Registration form"""

    email = StringField('email_label',
                           validators=[
                               InputRequired(message="Please enter email"),
                               Length(min=6, max=50, message="Please enter a valid mail"),
                               Email("Please enter a valid mail")
                           ])
    password = PasswordField('passwordn_label',
                             validators=[
                                 InputRequired(message="Please choose a password"),
                                 Length(min=6, message="Password must be at least 6 characters")
                             ])
    confirm_pswd = PasswordField('confirm_pswd_label',
                                 validators=[
                                     InputRequired(message="Please confirm your password"),
                                     EqualTo('password', message='password must match')
                                 ])
    submit_button = SubmitField('Sign up')

    # checks to see if user have entered unique email
    def validate_email(self, email):
        user_object = mds.User.query.filter_by(email=email.data).first()
        if user_object:
            raise ValidationError("Email already exists.")



class LoginForm(FlaskForm):
    """Login form"""

    email = StringField('email_label', validators=[InputRequired(message="Email Required")])
    password = PasswordField('password_label', validators=[InputRequired(message="Password Required"), invalid_credentials])
    submit_button = SubmitField('Login')


