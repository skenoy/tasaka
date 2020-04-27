# coding:utf-8
from flask import Blueprint, jsonify, request, json
from app.models import User
from app import auth, db, app
from uuid import uuid4
from app.utils import email

user = Blueprint('user', __name__)

@user.route("/validatecode", methods=['POST'])
def vc():
	data = request.json['data']
	email = User.query.filter(User.email==data['email']).first()
	if email:
		return jsonify({'msg': 'This email is exists!', 'code': 410})
	else:
		validatecode = ''
		while 1:
			validatecode = User.query.filter(User.validatecode==uuid4().hex).first()
			if not validatecode:
				break
		try:
			vc_user = User()
			vc_user.email = data['email']
			vc_user.validatecode = validatecode
			db.session.add(vc_user)
			db.session.commit()
			email('Tasaka邮箱验证', data['email'], 'sendcode', validatecode=validatecode)
		except:
			db.session.rollback()
			return jsonify({'msg': 'The database is error!', 'code': 411})
		return jsonify({'msg': 'Send email validate code！', 'code': 210})

	

	return jsonify(resp)

@user.route("/login", methods=['POST'])
def login():
    resp = {'msg': 'info', 'data': {}, 'token': ''}

    data = request.json['data']

    userinfo = User.query.filter_by(openid=openid).first()
    if not userinfo:
        r_user = User()
        r_user.name = data['nickName']
        r_user.gender = data['gender']
        r_user.city = data['city']
        r_user.province = data['province']
        r_user.country = data['country']
        r_user.img = data['avatarUrl']
        r_user.openid = openid

        db.session.add(r_user)
        db.session.commit()

        userinfo = r_user

    resp['data'] = userinfo.to_json()
    resp['msg'] = 'login / register success'
    resp['token'] = userinfo.generate_auth_token()

    return jsonify(resp)


@user.route("/check_token")
@auth.login_required
def token():
    return jsonify({'code': 201, 'msg': 'Check Token Success'})
