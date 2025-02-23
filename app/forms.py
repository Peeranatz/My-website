from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, URL

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message="Passwords must match")
    ])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SongForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    artist = StringField('Artist', validators=[DataRequired(), Length(max=100)])
    genre = StringField('Genre', validators=[DataRequired(), Length(max=50)])
    image_url = StringField('Image URL', validators=[URL(), Length(max=255)])  # เพิ่ม validation
    submit = SubmitField('Add Song')

class PlaylistForm(FlaskForm):
    name = StringField('Playlist Name', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Create Playlist')

class FavoriteGenreForm(FlaskForm):
    favorite_genre = StringField('Favorite Genre', validators=[DataRequired(), Length(max=50)])  # เพิ่ม validation
    submit = SubmitField('Save')