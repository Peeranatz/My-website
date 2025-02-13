from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=50)]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class SongForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    artist = StringField("Artist", validators=[DataRequired()])
    genre = StringField("Genre", validators=[DataRequired()])
    submit = SubmitField("Add Song")


class PlaylistForm(FlaskForm):
    name = StringField("Playlist Name", validators=[DataRequired()])
    submit = SubmitField("Create Playlist")
