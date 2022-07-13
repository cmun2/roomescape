from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'

client = MongoClient('mongodb+srv://test:sparta@cluster0.34r2eiy.mongodb.net/?retryWrites=true&w=majority')
db = client.roomescape

@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        return render_template('index.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


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
def detail():
    return render_template('detail.html')

@app.route("/users", methods=["POST"])
def save_comment():
    userid_receive = request.form['userID_give']
    comment_receive = request.form['comment_give']
    doc = {
        'userID': userid_receive,
        'comment': comment_receive
    }
    db.users.insert_one(doc)

    return jsonify({'msg':'후기 등록 완료'})

@app.route('/detail', methods=['POST'])
def get_map():
    gmaps = googlemaps.Client(key='AIzaSyBTNm1FSmfSnIa9ZakeUfLVXTo6bEd_W3c')
    geocode_result = gmaps.geocode('서울 마포구 서교동 338-48')
    if not geocode_result:
        return jsonify({'result': 'fail','msg': "Coudln't find the address on the map"})

    n_lat = geocode_result['geometry']['location']['lat']
    n_lng = geocode_result['geometry']['location']['lng']
    loc = {'lat': n_lat, 'lng': n_lng}

    print(loc)

if __name__ == '__main__':
    app.run('0.0.0.0', port=3000, debug=True)
