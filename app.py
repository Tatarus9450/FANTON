from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "บอทรันอยู่แล้วจ้า!"

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.json
    print("ได้รับข้อมูลจาก LINE:", body)  # Debugging
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
