# coding:utf-8
from flask import Blueprint, jsonify, request, send_from_directory, g
from app.models import Rare, User, Cancer
from app import auth, db
from sqlalchemy import or_

query = Blueprint('query', __name__)

@query.route("/queryInfo", methods=['POST'])
@auth.login_required
def queryInfo():
    user = User.query.filter(User.name == g.current_user).first()
    if user.snumber == 0 and user.email not in ['xuzijing86@163.com', 'sunyong@microanaly.com']:
        return jsonify({'msg': '搜索次数已使用完！', 'code': 0, 'snumber': 0})
    user.snumber -= 1
    db.session.commit()
    inputStr = request.json['input'].strip()
    diseaseType = request.json['type']
    if diseaseType == 'rare':
        res = Rare.query.filter(or_(Rare.diseasename.contains(inputStr), Rare.cause.contains(inputStr), Rare.drug.contains(inputStr))).all()
        if res:
            resjson = [i.to_json() for i in res]
            return jsonify({'msg': '获取成功！', 'code': 200, 'data': resjson, 'snumber': user.snumber})
        return jsonify({'msg': '没有找到数据！', 'code': 400})
    if diseaseType == 'cancer':
        res = Cancer.query.filter(or_(Cancer.diseasename.contains(inputStr), Cancer.geneother.contains(inputStr), Cancer.drug.contains(inputStr))).all()
        if res:
            resjson = [i.to_json() for i in res]
            return jsonify({'msg': '获取成功！', 'code': 200, 'data': resjson, 'snumber': user.snumber})
        return jsonify({'msg': '没有找到数据！', 'code': 400})


@query.route('/download', methods=['POST'])
@auth.login_required
def download():
    dfile = request.json['file']
    ftype = request.json['type']
    dirname = f'/opt/tasaka/flask/app/files/{ftype}/'

    return send_from_directory(dirname, dfile, as_attachment=True)