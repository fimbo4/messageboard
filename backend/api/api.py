from flask import Flask, request
import db

app = Flask(__name__)

@app.route("/add_message", methods=['POST', 'GET'])
def add_message():
    data = request.json
    db.insert_message(data.get("identity"), data.get("message"))
    return ""

@app.route("/get_message", methods=['POST', 'GET'])
def get_message():
    data = request.json
    return db.select_message(data.get("search_query"))

app.run(host='0.0.0.0', port=4001)