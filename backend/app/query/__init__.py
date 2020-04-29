# coding:utf-8
from flask import Blueprint, jsonify, request, send_from_directory
from app.models import Rare
from app import auth, db
from sqlalchemy import or_

query = Blueprint('query', __name__)

@query.route("/queryInfo", methods=['POST'])
@auth.login_required
def queryInfo():
    inputStr = request.json['input'].strip()
    diseaseType = request.json['type']
    if diseaseType == 'rare':
        res = Rare.query.filter(or_(Rare.diseasename.contains(inputStr), Rare.cause.contains(inputStr), Rare.drug.contains(inputStr))).all()
        if res:
            resjson = [i.to_json() for i in res]
            return jsonify({'msg': '获取成功！', 'code': 200, 'data': resjson})
        return jsonify({'msg': '没有找到数据！', 'code': 400})
    return jsonify({'msg': 'aaaa', 'code': 200})

@query.route('/download', methods=['POST'])
@auth.login_required
def download():
    dfile = request.json['file']
    ftype = request.json['type']
    dirname = f'/opt/tasaka/flask/app/files/{ftype}/'

    return send_from_directory(dirname, dfile, as_attachment=True)