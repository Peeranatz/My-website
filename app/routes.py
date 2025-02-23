from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Song, Playlist
from app.forms import RegistrationForm, LoginForm, SongForm, PlaylistForm, FavoriteGenreForm

main_routes = Blueprint('main', __name__)
auth_routes = Blueprint('auth', __name__)
song_routes = Blueprint('song', __name__)
playlist_routes = Blueprint('playlist', __name__)

@main_routes.route('/')
def index():
    """Redirect to login page if not authenticated, otherwise redirect to home."""
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    return redirect(url_for('auth.login'))

@main_routes.route('/home')
@login_required
def home():
    """Home page with paginated songs."""
    page = request.args.get('page', 1, type=int)
    per_page = 10
    songs = Song.query.paginate(page=page, per_page=per_page, error_out=False)
    return render_template('home.html', songs=songs)

@main_routes.route('/about')
def about():
    """About page."""
    return render_template('about.html')

@auth_routes.route('/register', methods=['GET', 'POST'])
def register():
    """User registration page."""
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    """User login page."""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Login failed. Check your username and password.', 'danger')
    return render_template('login.html', form=form)

@auth_routes.route('/logout')
@login_required
def logout():
    """User logout."""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

@playlist_routes.route('/playlists')
@login_required
def playlists():
    """Display user's playlists."""
    playlists = Playlist.query.filter_by(user_id=current_user.id).all()
    all_songs = Song.query.all()
    return render_template('playlists.html', playlists=playlists, all_songs=all_songs)

@playlist_routes.route('/create_playlist', methods=['GET', 'POST'])
@login_required
def create_playlist():
    """Create a new playlist."""
    form = PlaylistForm()
    if form.validate_on_submit():
        playlist = Playlist(name=form.name.data, user_id=current_user.id)
        db.session.add(playlist)
        db.session.commit()
        flash('Playlist created!', 'success')
        return redirect(url_for('playlist.playlists'))
    return render_template('create_playlist.html', form=form)

@song_routes.route('/songs')
@login_required
def songs():
    """Display all songs."""
    songs = Song.query.all()
    return render_template('songs.html', songs=songs)

@song_routes.route('/add_song', methods=['GET', 'POST'])
@login_required
def add_song():
    """Add a new song."""
    form = SongForm()
    if form.validate_on_submit():
        song = Song(title=form.title.data, artist=form.artist.data, genre=form.genre.data, image_url=form.image_url.data)
        db.session.add(song)
        db.session.commit()
        flash('Song added!', 'success')
        return redirect(url_for('song.songs'))
    return render_template('add_song.html', form=form)

@song_routes.route('/song/<int:song_id>')
def song_detail(song_id):
    """Display song details."""
    song = Song.query.get_or_404(song_id)
    return render_template('song_detail.html', song=song)

@playlist_routes.route('/add_to_playlist/<int:song_id>', methods=['POST'])
@login_required
def add_to_playlist(song_id):
    """Add a song to a playlist from the songs page."""
    try:
        playlist_id = request.form.get('playlist_id')
        playlist = Playlist.query.get_or_404(playlist_id)
        song = Song.query.get_or_404(song_id)
        
        if playlist.user_id != current_user.id:
            flash('ไม่อนุญาตให้เพิ่มเพลงในเพลย์ลิสต์นี้', 'danger')
            return redirect(url_for('song.songs'))
        
        playlist.songs.append(song)
        db.session.commit()
        flash('เพิ่มเพลงลงเพลย์ลิสต์สำเร็จ!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('เกิดข้อผิดพลาด กรุณาลองอีกครั้ง', 'danger')
    return redirect(url_for('song.songs'))

@playlist_routes.route('/add_song_to_playlist/<int:playlist_id>', methods=['POST'])
@login_required
def add_song_to_playlist(playlist_id):
    """Add a song to a playlist from the playlists page."""
    try:
        song_id = request.form.get('song_id')
        playlist = Playlist.query.get_or_404(playlist_id)
        song = Song.query.get_or_404(song_id)
        
        if playlist.user_id != current_user.id:
            flash('ไม่อนุญาตให้เพิ่มเพลงในเพลย์ลิสต์นี้', 'danger')
            return redirect(url_for('playlist.playlists'))
        
        playlist.songs.append(song)
        db.session.commit()
        flash('เพิ่มเพลงลงเพลย์ลิสต์สำเร็จ!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('เกิดข้อผิดพลาด กรุณาลองอีกครั้ง', 'danger')
    return redirect(url_for('playlist.playlists'))

@song_routes.route('/search')
def search():
    """Search for songs by title or artist."""
    query = request.args.get('query')
    if query:
        songs = Song.query.filter(
            (Song.title.contains(query)) | (Song.artist.contains(query))
        ).all()
    else:
        songs = Song.query.all()
    return render_template('songs.html', songs=songs)

@auth_routes.route('/update_favorite_genre', methods=['GET', 'POST'])
@login_required
def update_favorite_genre():
    """Update user's favorite genre."""
    form = FavoriteGenreForm()
    if form.validate_on_submit():
        current_user.favorite_genre = form.favorite_genre.data
        db.session.commit()
        flash('Favorite genre updated!', 'success')
        return redirect(url_for('auth.profile'))
    return render_template('profile.html', form=form)

@song_routes.route('/recommendations')
@login_required
def recommendations():
    """Display song recommendations based on user's favorite genre."""
    if current_user.favorite_genre:
        recommended_songs = Song.query.filter_by(genre=current_user.favorite_genre).all()
    else:
        recommended_songs = Song.query.all()
    return render_template('recommendations.html', songs=recommended_songs)

@auth_routes.route('/profile')
@login_required
def profile():
    """Display user profile."""
    form = FavoriteGenreForm()
    return render_template('profile.html', form=form)

@playlist_routes.route('/delete_playlist/<int:playlist_id>', methods=['POST'])
@login_required
def delete_playlist(playlist_id):
    """Delete a playlist."""
    playlist = Playlist.query.get_or_404(playlist_id)
    
    if playlist.user_id != current_user.id:
        flash('You do not have permission to delete this playlist.', 'danger')
        return redirect(url_for('playlist.playlists'))
    
    db.session.delete(playlist)
    db.session.commit()
    flash('Playlist deleted successfully!', 'success')
    return redirect(url_for('playlist.playlists'))