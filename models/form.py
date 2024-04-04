from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Regexp, Length


class LoginResetForm(FlaskForm):

    id = StringField(validators=[
        DataRequired(message="Id is required"),
        Regexp("^1[89]012[01][0-9]{3}$", message="Incorrect id format")])

    password = PasswordField(validators=[
        DataRequired(message="Password is required"),
        Length(min=8, max=30, message="Password must be 8-30 characters")])

    login = SubmitField()

    reset = SubmitField()
