
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

lm = LoginManager()
lm.setup_app(app)
lm.login_view = 'login'

import os
from flaskext.login import LoginManager
from flaskext.openid import OpenID
from config import basedir

lm = LoginManager()
lm.setup_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
