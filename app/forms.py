from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, SelectField, StringField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed


class ProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired("Please enter your firstname")])
    lastname  = StringField('Last Name', validators=[DataRequired("Please enter your lastname")])
    gender    = SelectField('Gender',validators=[DataRequired()], choices = [("", "Select Gender"),("Female", "Female"), ("Male", "Male")],)
    email     = StringField('Email', validators=[DataRequired("Please enter your e-mail address"), Email()])
    location  = StringField('Location', validators=[DataRequired("Please enter your location")])
    biography = TextAreaField("Biography", validators=[DataRequired("Please enter the message you would like to send")])
    photo     = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])