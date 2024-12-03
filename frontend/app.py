from flask import Flask, render_template, request
import requests
import json
import formatter
app = Flask(__name__)

messages = -1

@app.route("/")
def home():
    return render_template("home.html", data = messages)

@app.route("/post_message", methods=['POST', 'GET'])
def post_message():
    data = request.json
    response = requests.post("http://localhost:9001/post_database", json = data)
    return ""

@app.route("/search_message", methods=['POST', 'GET'])
def search_message():
    data = request.json
    response = requests.post("http://localhost:9002/retrieve_message", json = data)
    return ""

@app.route("/recieve_message", methods=['POST', 'GET'])
def recieve_message():
    global messages
    data = request.json
    html_code = ""
    for result in data:
        html_code += formatter.format(result, data[result])
    print(html_code)
    messages = html_code


    #messages = formatter.format(data)
    return ""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)