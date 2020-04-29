# coding:utf-8
from flask import Blueprint, jsonify, request
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