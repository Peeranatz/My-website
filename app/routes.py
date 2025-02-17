from flask import Blueprint, render_template, redirect, url_for, flash, request  # ลบ FavoriteGenreForm ออกจากนี้
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Song, Playlist
from app.forms import RegistrationForm, LoginForm, SongForm, PlaylistForm, FavoriteGenreForm  # เพิ่ม FavoriteGenreForm ที่นี่


main_routes = Blueprint('main', __name__)
auth_routes = Blueprint('auth', __name__)
song_routes = Blueprint('song', __name__)
playlist_routes = Blueprint('playlist', __name__)

@main_routes.route('/')
def home():
    return render_template('home.html')

@main_routes.route('/about')
def about():
    return render_template('about.html')

@auth_routes.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash('Login failed. Check your username and password.', 'danger')
    return render_template('login.html', form=form)

@auth_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@playlist_routes.route('/playlists')
@login_required
def playlists():
    playlists = Playlist.query.filter_by(user_id=current_user.id).all()
    return render_template('playlists.html', playlists=playlists)

@playlist_routes.route('/create_playlist', methods=['GET', 'POST'])
@login_required
def create_playlist():
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
    songs = Song.query.all()
    return render_template('songs.html', songs=songs)

@song_routes.route('/add_song', methods=['GET', 'POST'])
@login_required
def add_song():
    form = SongForm()
    if form.validate_on_submit():
        song = Song(title=form.title.data, artist=form.artist.data, genre=form.genre.data)
        db.session.add(song)
        db.session.commit()
        flash('Song added!', 'success')
        return redirect(url_for('song.songs'))
    return render_template('add_song.html', form=form)



@song_routes.route('/song/<int:song_id>')
def song_detail(song_id):
    song = Song.query.get_or_404(song_id)
    return render_template('song_detail.html', song=song)


@playlist_routes.route('/add_to_playlist/<int:song_id>', methods=['POST'])
@login_required
def add_to_playlist(song_id):
    playlist_id = request.form.get('playlist_id')  # รับค่า playlist_id จากฟอร์ม
    playlist = Playlist.query.get_or_404(playlist_id)  # ดึงข้อมูลเพลย์ลิสต์จากฐานข้อมูล
    song = Song.query.get_or_404(song_id)  # ดึงข้อมูลเพลงจากฐานข้อมูล
    playlist.songs.append(song)  # เพิ่มเพลงลงในเพลย์ลิสต์
    db.session.commit()  # บันทึกการเปลี่ยนแปลง
    flash('Song added to playlist!', 'success')  # แสดงข้อความแจ้งเตือน
    return redirect(url_for('song.song_detail', song_id=song_id))  # กลับไปหน้ารายละเอียดเพลง


@song_routes.route('/search')
def search():
    query = request.args.get('query')  # รับคำค้นหาจาก URL parameter
    if query:
        # ค้นหาเพลงโดยใช้ชื่อเพลงหรือศิลปิน
        songs = Song.query.filter(
            (Song.title.contains(query)) | (Song.artist.contains(query))
        ).all()
    else:
        songs = Song.query.all()  # ถ้าไม่มีคำค้นหา ให้แสดงเพลงทั้งหมด
    return render_template('songs.html', songs=songs)



@auth_routes.route('/update_favorite_genre', methods=['GET', 'POST'])
@login_required
def update_favorite_genre():
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
    if current_user.favorite_genre:
        # แนะนำเพลงตามประเภทเพลงที่ผู้ใช้ชอบ
        recommended_songs = Song.query.filter_by(genre=current_user.favorite_genre).all()
    else:
        # ถ้าผู้ใช้ยังไม่ได้เลือกประเภทเพลงที่ชอบ ให้แสดงเพลงทั้งหมด
        recommended_songs = Song.query.all()
    return render_template('recommendations.html', songs=recommended_songs)