# coding:utf-8
from flask import Blueprint, jsonify, request, json
from app.models import User
from app import auth, db, app
from uuid import uuid4
from app.utils import email

user = Blueprint('user', __name__)

@user.route("/validatecode", methods=['POST'])
def validatecode():
    data = request.json['data']
    emailObj = User.query.filter(User.email==data['email']).first()
    if emailObj:
        return jsonify({'msg': 'This email is exists!', 'code': 410})
    else:
        code = ''
        while 1:
            code = uuid4().hex
            codeObj = User.query.filter(User.validatecode==code).first()
            if not codeObj:
                break
        try:
            vc_user = User()
            vc_user.email = data['email']
            vc_user.validatecode = code
            db.session.add(vc_user)
            db.session.commit()
            # 单人发邮件也得是list
            email('Tasaka邮箱验证', [data['email']], 'sendcode', t_validatecode=code)
        except:
            db.session.rollback()
            return jsonify({'msg': 'The database is error!', 'code': 420})
        return jsonify({'msg': 'Send email validate code！', 'code': 200})

@user.route("/register", methods=['POST'])
def register():
    data = request.json['data']
    
    codeObj = User.query.filter(User.validatecode == data['validatecode']).first()
    if not codeObj:
        return jsonify({'msg': 'Email validate code is error!', 'code': 440})
    emailObj = User.query.filter(User.email == data['email']).first()
    if not codeObj:
        return jsonify({'msg': 'Email is error!', 'code': 450})
    nameObj = User.query.filter(User.name==data['name']).first()
    if nameObj:
        return jsonify({'msg': 'name is exists!', 'code': 430})
    try:
        r_user = User()
        r_user.name = data['name']
        r_user.email = data['email']
        r_user.validatecode = data['validatecode']
        r_user.password = r_user.hash_password(data['password'])
        db.session.add(r_user)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'msg': 'Add user fail！', 'code': 460})
    return jsonify({'msg': 'Add user success！', 'code': 200})

@user.route("/login", methods=['POST'])
def login():
    data = request.json['data']

    nameObj = User.query.filter(User.name==data['name']).first()
    if not nameObj:
        return jsonify({'msg': 'name is not exists!', 'code': 470})
    if nameObj.check_password(data['password']):
        token = nameObj.generate_auth_token()
        resp = {'token': token, 'name': data['name']}
        return jsonify({'msg': 'Login success!', 'code': 200, 'data':resp})

    return jsonify({'msg': 'Password is error!', 'code': 480})


@user.route("/check_token")
@auth.login_required
def token():
    return jsonify({'code': 200, 'msg': 'Check Token Success'})
