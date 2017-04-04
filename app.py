from flask import Flask, request, abort

from linebot import ( LineBotApi, WebhookHandler )
from linebot.exceptions import ( InvalidSignatureError )
from linebot.models import ( MessageEvent, TextMessage, TextSendMessage, )

import base64
import hashlib
import hmac

app = Flask(__name__)

Channel_ID = '1508575718'
Channel_Secret = '9de28e01b24c66a6a74411040097a619' # Channel secret string
Channel_Access_Token = 'wX48QUgber5AbF+6JcsrmtphuO807pZCWAjHYTEn2fnQTnbzfsxGB3bwC26Rs6fhCiyC1NFgR3ALswB00VLpTiA77FOsuWBZONuOUa++A2tVECw5fEVumyyTOYK212GhSYdkUNJZ8SREwcG45HKnIgdB04t89/1O/w1cDnyilFU='
userId = 'Ua19821cd93141008d26221f16381d256'

line_bot_api = LineBotApi(Channel_Access_Token)
handler = WebhookHandler(Channel_Secret)



@app.route('/')
def index():
    body = request.get_data(as_text=True) # Request body string
    hash = hmac.new(Channel_Secret.encode('utf-8'), body.encode('utf-8'), hashlib.sha256).digest()
    signatured = base64.b64encode(hash)
    # Compare X-Line-Signature request header and the signature    
    
    return signatured

@app.route("/callback", methods=['REQUEST'])
def callback():    

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run(debug=True)