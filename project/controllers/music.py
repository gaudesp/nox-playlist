from project import app
from flask import render_template, redirect, url_for
from project.models.music import Music
from project.validators.music import MusicValidator

@app.route('/', methods=["GET"])
@app.route('/music', methods=["GET"])
@app.route('/music/page/<int:page>/', methods=["GET"])
def music_index(page=1):
  nb = Music().count_all()
  paginate = Music().paginate_all(page, app.config['MUSIC_PER_PAGE'])
  musics = Music().fetch_all(page, app.config['MUSIC_PER_PAGE'])
  return render_template('music/index.html', paginate=paginate, musics=musics, nb=nb)

@app.route('/music/new/', methods=["GET", "POST"])
def music_new():
  if MusicValidator().on_create() == True:
    return redirect(url_for('music_index'))
  return render_template('music/new.html')

@app.route('/music/<string:slug>/', methods=["GET"])
def music_show(slug):
  if Music().fetch_by_slug(slug):
    music = Music().fetch_by_slug(slug)
    return render_template('music/show.html', music=music)
  return render_template('error/404.html')