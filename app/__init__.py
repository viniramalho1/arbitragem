from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/arbitragem'
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
