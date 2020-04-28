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
        return jsonify({'msg': '邮箱已存在！', 'code': 410})
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
            return jsonify({'msg': '录入数据库错误！', 'code': 420})
        return jsonify({'msg': '发送邮箱验证码成功！', 'code': 200})

@user.route("/register", methods=['POST'])
def register():
    data = request.json['data']
    userCode = User.query.filter(User.validatecode == data['validatecode']).first()
    if not userCode:
        return jsonify({'msg': '邮箱验证码不存在！', 'code': 490})
    userName = User.query.filter(User.name==data['username']).first()
    if userName:
        return jsonify({'msg': '用户名已存在！', 'code': 430})
    userEmail = User.query.filter(User.email == data['email']).first()
    if not userEmail:
        return jsonify({'msg': '邮箱不存在！', 'code': 450})
    else:
        if userEmail.validatecode != data['validatecode']:
            return jsonify({'msg': '验证码与邮箱不对应！', 'code': 440})
    try:
        userEmail.name = data['username']
        userEmail.password = userEmail.hash_password(data['password'])
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'msg': '添加用户失败！', 'code': 460})
    return jsonify({'msg': '添加用户成功', 'code': 200})

@user.route("/login", methods=['POST'])
def login():
    data = request.json['data']

    userName = User.query.filter(User.name==data['username']).first()
    if not userName:
        return jsonify({'msg': '用户名不存在！', 'code': 470})
    if userName.check_password(data['password']):
        token = userName.generate_auth_token()
        resp = {'token': token, 'username': data['username']}
        return jsonify({'msg': '登陆成功！', 'code': 200, 'data':resp})
    return jsonify({'msg': '密码错误！', 'code': 480})

@user.route("/check_token")
@auth.login_required
def token():
    return jsonify({'code': 200, 'msg': 'Check Token Success'})
