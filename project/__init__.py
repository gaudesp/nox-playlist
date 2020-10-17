__version__ = '0.1'

import sys
from flask import Flask
from flask_turbolinks import turbolinks
from flask_fontawesome import FontAwesome
from project.models.database import db

app = Flask('project')
fa = FontAwesome(app)

turbolinks(app)

app.config.from_object('config')
app.debug = True

db.init_app(app)

from project.controllers import *
