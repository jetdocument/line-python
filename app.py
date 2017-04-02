from flask import Flask
import json
import requests

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError



app = Flask(__name__)

@app.route("/")
def hello():
	line_bot_api = LineBotApi('wX48QUgber5AbF+6JcsrmtphuO807pZCWAjHYTEn2fnQTnbzfsxGB3bwC26Rs6fhCiyC1NFgR3ALswB00VLpTiA77FOsuWBZONuOUa++A2tVECw5fEVumyyTOYK212GhSYdkUNJZ8SREwcG45HKnIgdB04t89/1O/w1cDnyilFU=')

try:
    line_bot_api.reply_message('<reply_token>', TextSendMessage(text='Hello World!'))
except LineBotApiError as e:
	
    return "OK!"

@app.route('/callback', methods=['POST'])
def callback():
	return '',200

if __name__ == "__main__":
    app.run()
