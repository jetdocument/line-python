from flask import Flask, requesst
import json
import requests

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

app = Flask(__name__)

@app.route("/")
def hello():
    return "OK!"

@app.route('/callback', methods=['POST'])
def callback():
	return '',200

if __name__ == "__main__":
    app.run()
