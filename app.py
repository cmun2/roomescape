from flask import Flask, render_template, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pymongo import MongoClient
from time import sleep
import requests

<<<<<<< HEAD
=======
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'

>>>>>>> origin/master
client = MongoClient('mongodb+srv://test:sparta@cluster0.34r2eiy.mongodb.net/?retryWrites=true&w=majority')
db = client.roomescape
app = Flask(__name__)
#
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#

# 1번크롤링
# data = requests.get('https://www.roomescape.co.kr/store/main.php', headers=headers)
# url = "https://www.roomescape.co.kr/store/main.php"
# driver = webdriver.Chrome('./chromedriver')
# driver.set_window_size(1920, 1080)
# driver.get(url)
# sleep(3)
#
# element = driver.find_element(By.CLASS_NAME, 'loc > ul > li:nth-child(53) > span')
# element.click()
# element = driver.find_element(By.ID, 'search_btn')
# element.click()
# sleep(1)
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
#         'address': '제주'
#     }
#     # db.stores.insert_one(doc)


@app.route('/')
def home():
    return render_template('index.html')


<<<<<<< HEAD
@app.route("/store", methods=["GET"])
def listing():
    stores_list = list(db.stores.find({}, {'_id': False}))
    return jsonify({'stores': stores_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
=======
@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)

@app.route('/sign_in', methods=['POST'])
def sign_in():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,
        "password": password_hash
    }

    db.users.insert_one(doc)
    return jsonify({'result': 'success'})

@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})


@app.route('/detail')
def page2():
    return render_template('detail.html')


@app.route("/users", methods=["POST"])
def save_comment():
    userid_receive = request.form['userID_give']
    comment_receive = request.form['comment_give']
    doc = {
        'userID': userid_receive,
        'comment': comment_receive
    }
    db.comments.insert_one(doc)

    return jsonify({'msg':'후기 등록 완료'})


@app.route("/users", methods=["GET"])
def show_comment():
    comment_list = list(db.comments.find({}, {'_id': False}))
    return jsonify({'comments':comment_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
>>>>>>> origin/master
