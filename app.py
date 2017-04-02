# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
import json
import requests

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

import os

app = Flask(__name__)

@app.route("/")
def hello():
	line_bot_api = LineBotApi('wX48QUgber5AbF+6JcsrmtphuO807pZCWAjHYTEn2fnQTnbzfsxGB3bwC26Rs6fhCiyC1NFgR3ALswB00VLpTiA77FOsuWBZONuOUa++A2tVECw5fEVumyyTOYK212GhSYdkUNJZ8SREwcG45HKnIgdB04t89/1O/w1cDnyilFU=')
	
	hostname = "google.com" #example
	response = os.system("ping " + hostname)
	#and then check the response...
	if response == 0:
	  line_bot_api.push_message('Ua19821cd93141008d26221f16381d256', TextSendMessage(text=hostname+' : '+'Link\'s Up เข้าถึงได้'))
	else:
	  line_bot_api.push_message('Ua19821cd93141008d26221f16381d256', TextSendMessage(text=hostname+' : '+'Link\'s Down ไม่สามารถเข้าถึงได้'))	

    	return "OK!"

@app.route('/callback', methods=['POST'])
def callback():
	return '',200

if __name__ == "__main__":
    app.run()
