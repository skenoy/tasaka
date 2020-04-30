# coding: utf-8
#用来创建数据库模型
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sys import argv

app = Flask(__name__)
app.config.from_pyfile('./config.py')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(32), index=True, unique=True)
    _password = db.Column(db.String(100))
    validatecode = db.Column(db.String(32))
    snumber = db.Column(db.Integer, default=5)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
  
class Rare(db.Model):
    __tablename__ = "rare"
    id = db.Column(db.Integer, primary_key=True)
    zhid = db.Column(db.String(6))
    diseasename = db.Column(db.String(32), index=True)
    cause = db.Column(db.String(100), index=True)
    drug = db.Column(db.String(64), index=True)
    approval = db.Column(db.String(32))

if __name__ == '__main__':
    db.create_all()
    # with open(argv[1]) as rarefile:
    #     for i in rarefile:
    #         tmp = i.split()
    #         rare = Rare(zhid=tmp[0], diseasename=tmp[1], cause=tmp[2], drug=tmp[3], approval=tmp[4])
    #         db.session.add(rare)
    #         db.session.commit()
    

