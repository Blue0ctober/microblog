import os
from flaskext.login import LoginManager
from flaskext.openid import OpenID
from config import basdir

lm = LoginManager()
lm.setup_app(app)
oid = OpenID(app, os.path.join(basdir, 'tmp'))

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

