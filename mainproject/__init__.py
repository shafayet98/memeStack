import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate  import Migrate
from flask_login import LoginManager

app = Flask(__name__)

# form configure
app.config['SECRET_KEY'] = 'fskey'

###############################
####### Database Setup ########
###############################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

###############################
#### Login Config Setup #######
###############################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

from mainproject.core.views import core
from mainproject.error_pages.views import error_pages


app.register_blueprint(core)
app.register_blueprint(error_pages)

