# conda 로 인터프리터 연결하기
# conda install flask, flask-cors, requests
#

from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
import openai

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

@app.route("/gpt-test", methods=['post'])
def gpt_test():
    data = {
        'userNo': 1
    }
    os.environ["OPENAI_API_KEY"] = "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"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": "지피티야 너는 철학에 대해서 어떻게 생각하니?"}
      ]
    )
    return completion.choices[0].message;

@app.route("/question-for-haru", methods=['post'])
def question_gpt():
    params = request.get_json()
    os.environ["OPENAI_API_KEY"] = "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"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": params['question']}
      ]
    )
    return completion.choices[0].message;

if __name__ == '__main__':
    app.run();


    # git remote add origin https://github.com/onedaythink/onedaythink_backend_flask.git
    # git branch -M '자기이름'
    # git branch -u origin '본인이름'
    #