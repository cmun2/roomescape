# from pymongo import MongoClient
# import jwt
# import datetime
# import hashlib
# from flask import Flask, render_template, jsonify, request, redirect, url_for
# from werkzeug.utils import secure_filename
# from datetime import datetime, timedelta
#
#
# app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True
# app.config['UPLOAD_FOLDER'] = "./static/profile_pics"
#
# SECRET_KEY = 'SPARTA'
#
# # client = MongoClient('내AWS아이피', 27017, username="아이디", password="비밀번호")
# # db = client.dbsparta_plus_week4
#
# client = MongoClient('mongodb+srv://test:sparta@cluster0.mja2a.mongodb.net/?retryWrites=true&w=majority')
# db = client.roomescape
#
# @app.route('/')
# def home():
#     token_receive = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#
#         return render_template('index.html')
#     except jwt.ExpiredSignatureError:
#         return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
#     except jwt.exceptions.DecodeError:
#         return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))
#
#
# @app.route('/login')
# def login():
#     msg = request.args.get("msg")
#     return render_template('login.html', msg=msg)
#
#
# @app.route('/user/<username>')
# def user(username):
#     # 각 사용자의 프로필과 글을 모아볼 수 있는 공간
#     token_receive = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         status = (username == payload["id"])  # 내 프로필이면 True, 다른 사람 프로필 페이지면 False
#
#         user_info = db.users.find_one({"username": username}, {"_id": False})
#         return render_template('user.html', user_info=user_info, status=status)
#     except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
#         return redirect(url_for("home"))
#
#
# @app.route('/sign_in', methods=['POST'])
# def sign_in():
#     # 로그인
#     return jsonify({'result': 'success'})
#
#
# @app.route('/sign_up/save', methods=['POST'])
# def sign_up():
#     # 회원가입
#     username_receive = request.form['username_give']
#     password_receive = request.form['password_give']
#     password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
#     # DB에 저장
#     return jsonify({'result': 'success'})
#
#
# @app.route('/sign_up/check_dup', methods=['POST'])
# def check_dup():
#     # ID 중복확인
#     return jsonify({'result': 'success'})
#
#
# @app.route('/update_profile', methods=['POST'])
# def save_img():
#     token_receive = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         # 프로필 업데이트
#         return jsonify({"result": "success", 'msg': '프로필을 업데이트했습니다.'})
#     except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
#         return redirect(url_for("home"))
#
#
# @app.route('/posting', methods=['POST'])
# def posting():
#     token_receive = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         # 포스팅하기
#         return jsonify({"result": "success", 'msg': '포스팅 성공'})
#     except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
#         return redirect(url_for("home"))
#
#
# @app.route("/get_posts", methods=['GET'])
# def get_posts():
#     token_receive = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         # 포스팅 목록 받아오기
#         return jsonify({"result": "success", "msg": "포스팅을 가져왔습니다."})
#     except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
#         return redirect(url_for("home"))
#
#
# @app.route('/update_like', methods=['POST'])
# def update_like():
#     token_receive = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         # 좋아요 수 변경
#         return jsonify({"result": "success", 'msg': 'updated'})
#     except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
#         return redirect(url_for("home"))
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=3000, debug=True)

import requests

from flask import Flask, render_template, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pymongo import MongoClient
from time import sleep

client = MongoClient('mongodb+srv://changsoon:tnsrh124!1@cluster0.ry8gyso.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta_roomEscape
app = Flask(__name__)
#
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#

# 1번크롤링
# data = requests.get('https://www.roomescape.co.kr/store/main.php', headers=headers)
# url = "https://www.roomescape.co.kr/store/main.php"
# driver = webdriver.Chrome('./chromedriver')
# driver.get(url)
# sleep(5)
#
# for i in range(15):
#     element = driver.find_element(By.ID, 'company_list_more_btn')
#     element.click()
#     sleep(1)
#
# req = driver.page_source
# soup = BeautifulSoup(req, 'html.parser')
# stores = soup.select('#company_list_row > div > div.ratio > div')
# for store in stores:
#     name = store.select_one('div > div.name > span > a').text
#     img = store.select_one('div > div.info > div.pic')['style']
#     num = img[-9:-6].strip('/')
#     print(name, img, num)
#
#     doc = {
#         'name': name,
#         'img': img,
#         'num': num,
#         'address': '0'
#     }
#     db.store.insert_one(doc)

# 2번크롤링
# url = 'https://www.roomescape.co.kr/store/detail.php'
# alllist = db.store.find({'num': {'$gt': '0'}}, {'_id': False, 'num': True})
# for i in alllist:
#     data = requests.get(url, params={'cafe': i["num"]}, headers=headers)
#     soup = BeautifulSoup(data.text, 'html.parser')
#     address = soup.select(
#         'body > div.container > div.container_inner.section.section_det_info > div > div.det_info_inner.loc')
#     for ads in address:
#         loc = ads.select_one('div.loc_info > div.address > span.text.value').text[0:2]
#         db.store.update_many({}, {'$set': {'address': loc}})


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/store", methods=["GET"])
def listing():
    store_list = list(db.store.find({}, {'_id': False}))
    return jsonify({'store': store_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
