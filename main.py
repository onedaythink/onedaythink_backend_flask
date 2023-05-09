# conda 로 인터프리터 연결하기
# conda install flask, flask-cors, requests
#



from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__);
CORS(app, supports_credentials=True);


@app.route("/")
def hello_word():
    data = {'name': 'taekyeong'}
    return jsonify(data);


@app.route("/test", methods=['GET'])
def test():
    addr = "http://localhost:8080/onedaythink/";
    data = {'name': 'taekyeong'}
    response = requests.get(addr+"flask/v1/test")
    data = {
        'userNo': 1
    }
    res = requests.post(addr+"flask/v1/post-test")
    print(response.text)
    print(res.text)
    return jsonify(res.text)


if __name__ == '__main__':
    app.run();