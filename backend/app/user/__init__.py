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
	email = User.query.filter(User.email==data['email']).first()
	if email:
		return jsonify({'msg': 'This email is exists!', 'code': 410})
	else:
		code = ''
		while 1:
			code = User.query.filter(User.validatecode==uuid4().hex).first()
			if not code:
				break
		try:
			vc_user = User()
			vc_user.email = data['email']
			vc_user.validatecode = code
			db.session.add(vc_user)
			db.session.commit()
			email('Tasaka邮箱验证', data['email'], 'sendcode', validatecode=code)
		except:
			db.session.rollback()
			return jsonify({'msg': 'The database is error!', 'code': 420})
		return jsonify({'msg': 'Send email validate code！', 'code': 200})

@user.route("/register", methods=['POST'])
def register():
    data = request.json['data']
	
    code = User.query.filter(User.validatecode == data['validatecode']).first()
    if not code:
        return jsonify({'msg': 'Email validate code is error!', 'code': 440})
    email = User.query.filter(User.email == data['email']).first()
    if not code:
        return jsonify({'msg': 'Email is error!', 'code': 450})
	name = User.query.filter(User.name==data['name']).first()
    if name:
        return jsonify({'msg': 'name is exists!', 'code': 430})
    try:
        r_user = User()
        r_user.name = name
        r_user.email = email
        r_user.validatecode = code
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

    name = User.query.filter(User.name==data['name']).first()
    if not name:
        return jsonify({'msg': 'name is not exists!', 'code': 470})
    if name.check_password(data['password']):
        token = name.generate_auth_token()
        resp = {'token': token, 'name': name}
        return jsonify({'msg': 'Login success!', 'code': 200, 'data':resp})

    return jsonify({'msg': 'Password is error!', 'code': 480})


@user.route("/check_token")
@auth.login_required
def token():
    return jsonify({'code': 200, 'msg': 'Check Token Success'})
