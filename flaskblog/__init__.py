from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '3771810e5aaf948dbf0d575b37d31533'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
# configure mail
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True   
app.config['MAIL_USERNAME'] = 'curtismensah48@gmail.com'
app.config['MAIL_PASSWORD'] = 'ipwfxbnoqyuhouwl'
# testing
# app.config['MAIL_DEBUG'] = True   
# app.config['MAIL_SUPPRESS_SEND'] = False   
# app.config['TESTING'] = False   
mail = Mail(app)

from flaskblog import routes