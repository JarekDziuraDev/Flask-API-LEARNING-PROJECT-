from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# result = db.session.execute('show databases')
#
# for res in result:
#     print(res)

from book_library_app import authors
from book_library_app import model
from book_library_app import db_manage_commands


# @app.route('/')
# def index():
#     return 'hello!!!'