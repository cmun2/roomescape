# import jwt
# import datetime
# import hashlib
from flask import Flask, render_template, request, jsonify
# from werkzeug.utils import secure_filename
# from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup


app = Flask(__name__)
#app.config["TEMPLATES_AUTO_RELOAD"] = True
#app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

#SECRET_KEY = 'SPARTA'

# client = MongoClient('내AWS아이피', 27017, username="아이디", password="비밀번호")
# db = client.dbsparta_plus_week4

# client = MongoClient('mongodb+srv://test_changsoon:sparta@cluster0.34r2eiy.mongodb.net/?retryWrites=true&w=majority')
# db = client.roomescape
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.34r2eiy.mongodb.net/?retryWrites=true&w=majority')
db = client.roomescape



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = "https://www.roomescape.co.kr/store/detail.php"

num_list = list(db.stores.find({}, {"_id": False, "name": False, "img": False, "address": False}))
#rint(num_list[0]['num'])
#num_list[i]['num']
for i in range(len(num_list)):
    data = requests.get(url, params={'cafe': num_list[i]['num']}, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')


    # desc = soup.select_one(
    #     'body > div.container > div.container_inner.section.section_det_info > div > div.det_info_inner.intro > div.desc > p > span').text.strip()
    # if desc is None:
    #     desc = '정보가 없어요'
    # else:
    #     desc = desc
    #
    # image = soup.select_one('body > div.container > div.container_inner.section.section_det_info > div > div.det_info_inner.theme_info > div.theme_list > div:nth-child(1) > div > div.pic')
    #
    # if image is not None:
    #     image = soup.select_one(
    #         'body > div.container > div.container_inner.section.section_det_info > div > div.det_info_inner.theme_info > div.theme_list > div:nth-child(1) > div > div.pic')[
    #                 'style'][21:-2]
    # else:
    #     image = '이미지 준비중'
    #
    # info_tag = soup.select_one('body > div.container > div.container_inner.section.section_det_info > div > div.det_info_inner.theme_info > div.theme_list > div:nth-child(1) > div > div.info > div.name.font_fit_div > p > span > a')
    # if info_tag is not None:
    #     info_tag = soup.select_one(
    #         'body > div.container > div.container_inner.section.section_det_info > div > div.det_info_inner.theme_info > div.theme_list > div:nth-child(1) > div > div.info > div.name.font_fit_div > p > span > a').text
    #
    # else:
    #     info_tag = ''
    #
    # genre = soup.select_one('body > div.container > div.container_inner.section.section_det_info > div > div.det_info_inner.theme_info > div.theme_list > div:nth-child(1) > div > div.info > div.genre_n_star > span.text.genre')
    # if genre is not None:
    #     genre = soup.select_one(
    #         'body > div.container > div.container_inner.section.section_det_info > div > div.det_info_inner.theme_info > div.theme_list > div:nth-child(1) > div > div.info > div.genre_n_star > span.text.genre').text
    # else:
    #     genre = ''
    #
    # phone = soup.select_one(
    #     'body > div.container > div.container_inner.section.section_det_info > div > div.det_info_inner.loc > div.loc_info > div.phone > span.text.value').text
    # if phone is None:
    #     phone = '정보가 없어요'
    # else:
    #     phone = phone
    # address = soup.select_one(
    #     'body > div.container > div.container_inner.section.section_det_info > div > div.det_info_inner.loc > div.loc_info > div.address > span.text.value').text
    # if address is None:
    #     address = '정보가 없어요'
    # else:
    #     address = address
    # fee = soup.select_one(
    #     'body > div.container > div.container_inner.section.section_det_info > div > div.det_info_inner.fee > div.fee_info').text
    # if fee is None:
    #     fee = '정보가 없어요'
    # else:
    #     fee = fee
    #
    # doc = {
    #     'desc': desc,
    #     'image': image,
    #     'info_tag': info_tag,
    #     'genre': genre,
    #     'phone': phone,
    #     'address': address,
    #     'fee': fee,
    #     'num': num_list[i]['num']
    # }
    # db.details2.insert_one(doc)


# data = requests.get('https://www.roomescape.co.kr/store/detail.php?cafe=405', headers=headers)
# soup = BeautifulSoup(data.text, 'html.parser')


#db.miniproject.insert_one(doc)
@app.route('/')
def home():
    return render_template('detail.html')

@app.route("/detail", methods=["GET"])
def listing():
    detail_list = list(db.details2.find({}, {'_id': False}))
    return jsonify({'detail': detail_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)



#print(desc.text.strip(), info_tag.text.strip(), genre.text.strip(), phone.text.strip(), address.text.strip(), fee.text)
# themes = soup.select('#body > div.container > div.container_inner.section.section_det_info > div > div.det_info_inner.intro')
# for theme in themes:
#     a = theme.select_one('div.desc > p > span')
#     if a is not None:
#         print(a)


#desc = soup.select(body > div.container > div.container_inner.section.section_det_info > div > div.det_info_inner.intro > div.desc > p > span)
# @app.route('/detail', methods=["POST"])
# def detail_post():


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
 # if __name__ == '__main__':
 #    app.run('0.0.0.0', port=5000, debug=True)