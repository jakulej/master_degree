from flask import Flask, request, jsonify
import time
app = Flask(__name__)

@app.route("/", methods=["POST"])
def hello_world():
    data = request.get_json()
    time.sleep(1)
    return "<p>Hello, World!</p>"
