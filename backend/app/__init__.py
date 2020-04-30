from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth
from flask_cors import CORS
from flask_mail import Mail

app = Flask(__name__)
app.config.from_pyfile('./config.py')

CORS(app)
mail = Mail(app)
db = SQLAlchemy()
db.app = app
db.init_app(app)
auth = HTTPTokenAuth(scheme='Token')

# 所有对象要在注册之前初始化，否则找不到该对象
from app.user import user
from app.query import query

app.register_blueprint(user, url_prefix="/api/user")
app.register_blueprint(query, url_prefix="/api/query")
