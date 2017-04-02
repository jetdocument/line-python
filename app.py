from flask import Flask
import json
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "OK!"

@app.route('/callback', methods=['POST'])
def callback():
	json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    #id=[d['replyToken'] for d in user][0]
    #print(json_line)
    print("ผู้ใช้：",user)
    sendText(user,'งง')
	return '',200

if __name__ == "__main__":
    app.run()
