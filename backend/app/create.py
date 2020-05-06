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

class Cancer(db.Model):
    __tablename__ = "cancer"
    id = db.Column(db.Integer, primary_key=True)
    zhid = db.Column(db.String(6))
    diseasename = db.Column(db.String(32), index=True)
    geneother = db.Column(db.String(32), index=True)
    gene_type = db.Column(db.String(32))
    sample = db.Column(db.String(32))
    sample_approval = db.Column(db.String(32))
    drug = db.Column(db.String(100), index=True)
    drup_effect = db.Column(db.String(32))
    nation_approval = db.Column(db.String(32))
    other = db.Column(db.String(100))

if __name__ == '__main__':
    db.create_all()
    # with open(argv[1]) as rarefile:
    #     for i in rarefile:
    #         tmp = i.split()
    #         rare = Rare(zhid=tmp[0], diseasename=tmp[1], cause=tmp[2], drug=tmp[3], approval=tmp[4])
    #         db.session.add(rare)
    #         db.session.commit()

    # with open(argv[1]) as cancerfile:
    #     for i in cancerfile:
    #         tmp = i.split()
    #         cancer = Rare(zhid=tmp[0], diseasename=tmp[1], geneother=tmp[2], gene_type=tmp[3], sample=tmp[4], sample_approval=tmp[5], drug=tmp[6], drup_effect=tmp[7], nation_approval=tmp[8], other=tmp[9])
    #         db.session.add(cancer)
    #         db.session.commit()
    
    # User.query.update({'snumber': 5})
    # db.session.commit()

