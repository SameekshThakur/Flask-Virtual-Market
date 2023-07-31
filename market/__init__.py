from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SECRET_KEY'] = '7140dddcb334c6d249a26fb4'  # Generating the secret key is important as it helps in creating a security layer over the falsk application when user registers or post some data in our app. Without using secret key we cannot use flask forms as well.
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
app.app_context().push()

from market import routes
