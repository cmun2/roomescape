from flask import Flask, render_template, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pymongo import MongoClient
from time import sleep
import requests

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


@app.route("/store", methods=["GET"])
def listing():
    stores_list = list(db.stores.find({}, {'_id': False}))
    return jsonify({'stores': stores_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
