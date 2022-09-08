from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'b234f6c72e48de049ada25a011defee9'
db = SQLAlchemy(app)

from flaskblog import routes