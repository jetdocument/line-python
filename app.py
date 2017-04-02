from flask import Flask
import json
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "OK!"

@app.route('/callback', methods=['POST'])
def callback():
	return '',200

if __name__ == "__main__":
    app.run()
