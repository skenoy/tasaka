# coding: utf-8
##用来创建数据库模型
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#app = Flask(__name__)
#app.config.from_pyfile('./config.py')
#db = SQLAlchemy(app)


from app import db, auth
from flask import current_app, jsonify, g
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from werkzeug.security import generate_password_hash, check_password_hash

@auth.error_handler
def error_handler():
    return jsonify({'code':401, 'msg':'Unauthorized Access'})

@auth.verify_token
def verify_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        return False
    except BadSignature:
        return False
    g.current_user = data['name']
    return True


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(32), index=True, unique=True)
    _password = db.Column(db.String(100))
    validatecode = db.Column(db.String(32))
    snumber = db.Column(db.Integer, default=5)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def generate_auth_token(self):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=3600)
        return str(s.dumps({'vc': self.validatecode, 'name': self.name}), encoding='utf-8')
    
    def hash_password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, pwd):
        return check_password_hash(self._password, pwd)

class Rare(db.Model):
    __tablename__ = "rare"
    id = db.Column(db.Integer, primary_key=True)
    zhid = db.Column(db.String(6))
    diseasename = db.Column(db.String(32), index=True)
    cause = db.Column(db.String(100), index=True)
    drug = db.Column(db.String(64), index=True)
    approval = db.Column(db.String(32))

    def to_json(self):
        return {
            'id': self.id,
            'zhid': f'{self.zhid}.pdf',
            'diseasename': self.diseasename,
            'cause': self.cause,
            'drug': self.drug,
            'approval': self.approval
        }

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

    def to_json(self):
        return {
            'id': self.id,
            'zhid': f'{self.zhid}.pdf',
            'diseasename': self.diseasename,
            'geneother': self.geneother,
            'gene_type': self.gene_type,
            'sample': self.sample,
            'sample_approval': self.sample_approval,
            'drug': self.drug,
            'drup_effect': self.drup_effect,
            'nation_approval': self.nation_approval,
            'other': self.other
        }

if __name__ == '__main__':
    db.create_all()
