from project.models.database import db
from datetime import datetime
from slugify import slugify

class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def insert_all(self, video, title):
        music = Music(video=video, title=title, slug=slugify(title), created_at=datetime.now())
        db.session.add(music)
        db.session.commit()

    def fetch_all(self, page=0, per_page=None):
        musics = Music.query.order_by(Music.id.desc()).limit(per_page).offset((page-1)*per_page)
        return musics

    def fetch_by_video(self, video):
        music = Music.query.filter(Music.video == video).first()
        return music

    def fetch_by_slug(self, slug):
        music = Music.query.filter(Music.slug == slug).first()
        return music

    def paginate_all(self, page=0, per_page=None):
        musics = Music.query.order_by(Music.id.desc()).paginate(page, per_page)
        return musics

    def count_all(self):
        music = Music.query.count()
        return music
