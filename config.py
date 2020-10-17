import os
from os.path import join, dirname, realpath

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

MUSIC_PER_PAGE = 15