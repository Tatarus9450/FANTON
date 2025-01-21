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
    port = int(os.environ.get("PORT", 5000))  # ดึง PORT จาก Railway ถ้าไม่มีให้ใช้ 5000
    app.run(host="0.0.0.0", port=port, debug=True)
