from flask import Flask, render_template, url_for, request
import requests
import json
app = Flask(__name__)

@app.route("/")
def home():
    #response = requests.get("http://127.0.0.1:9001/test")
    #print(response.text)
    return render_template("home.html")

@app.route("/post_message", methods=['POST', 'GET'])
def post_message():
    data = request.json
    response = requests.post("http://127.0.0.1:1313/post_database", json = data)
    return ""

@app.route("/search_message", methods=['POST', 'GET'])
def search_message():
    data = request.json
    response = requests.post("http://127.0.0.1:9002/retrieve_message", json = data)
    return ""

@app.route("/recieve_message", methods=['POST', 'GET'])
def recieve_message():
    data = request.json
    print(data)
    return ""

if __name__ == '__main__':
    app.run(debug=True, port=5001)