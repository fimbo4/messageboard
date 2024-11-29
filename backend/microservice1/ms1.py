from flask import Flask, request
import requests
app = Flask(__name__)

@app.route("/post_database", methods=['POST', 'GET'])
def post_database():
    print("lololololololololololololol", flush=True)
    data = request.json
    print(data.get("identity"), flush=True)
    response = requests.post("http://api:4001/add_message", json = data)
    return ""

app.run(host='0.0.0.0', port=9001)