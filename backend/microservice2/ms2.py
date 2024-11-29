import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/retrieve_message", methods=['POST', 'GET'])
def rertrieve_data():
    search_query = request.json
    print(search_query, flush=True)
    response = requests.post("http://127.0.0.1:4000/get_message", json = search_query)
    print("ms2 responmse", flush=True)
    print(response.text, flush=True)
    send_response = requests.post("http://127.0.0.1:5001/recieve_message", json = response.text)
    return ""

app.run(host='0.0.0.0', port=9002)