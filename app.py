from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "บอทรันอยู่แล้วจ้า!"

@app.route("/webhook", methods=["POST"])  # รองรับเฉพาะ POST
def webhook():
    body = request.json
    print("📩 ได้รับข้อมูลจาก LINE:", body)  # Debugging
    return jsonify({"status": "ok"})  # ส่ง HTTP 200 กลับไป

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
