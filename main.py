from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
import openai

app = Flask(__name__);
CORS(app, supports_credentials=True);

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

