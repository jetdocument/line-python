# -*- coding: utf-8 -*-

from flask import Flask, request, abort

from linebot import ( LineBotApi, WebhookHandler ) 
from linebot.exceptions import ( InvalidSignatureError )
from linebot.models import ( MessageEvent, TextMessage, TextSendMessage )

app = Flask(__name__)

line_bot_api = LineBotApi('wX48QUgber5AbF+6JcsrmtphuO807pZCWAjHYTEn2fnQTnbzfsxGB3bwC26Rs6fhCiyC1NFgR3ALswB00VLpTiA77FOsuWBZONuOUa++A2tVECw5fEVumyyTOYK212GhSYdkUNJZ8SREwcG45HKnIgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('51d99670e2bb8acd7433e7bf75fb5416')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    handler.handle(body, signature)  

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
