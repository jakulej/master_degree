from flask import Flask, request, jsonify
import time
app = Flask(__name__)

@app.route("/", methods=["POST"])
def get_json():
    data = request.get_json()
    return "OK",200

@app.route("/file", methods=["POST"])
def get_file():
    file = request.files["file"]
    return "OK",200
