from flask import Flask
import json
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "READY!"

@app.route('/callback', methods=['POST'])
def callback():
	return '',200

if __name__ == "__main__":
    app.run()
