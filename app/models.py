from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.query.get(int(user_id))

# ประกาศตารางกลางก่อน
playlist_song = db.Table('playlist_song',
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlist.id'), primary_key=True),
    db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True)
)

class Song(db.Model):
    """Song model."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(255))  # URL รูปภาพของเพลง

    # ความสัมพันธ์หลายต่อหลายกับ Playlist
    playlists = db.relationship('Playlist', secondary=playlist_song, back_populates='songs')

class Playlist(db.Model):
    """Playlist model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # ความสัมพันธ์หลายต่อหลายกับ Song
    songs = db.relationship('Song', secondary=playlist_song, back_populates='playlists')

class User(db.Model, UserMixin):
    """User model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    favorite_genre = db.Column(db.String(50))  # เพิ่มฟิลด์แนวเพลงที่ชอบ
    
    # ความสัมพันธ์กับ Playlist
    playlists = db.relationship('Playlist', backref='user', lazy=True)