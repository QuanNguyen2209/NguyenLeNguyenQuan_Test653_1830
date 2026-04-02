import os
from flask import Flask, render_template, request, jsonify

# IMPORT CẢ 2 THUẬT TOÁN
from cipher.transposition.transposition_cipher import TranspositionCipher
from cipher.ecc.ecc_cipher import ECCCipher

# CẤU HÌNH ĐƯỜNG DẪN
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

# =========================
# TRANG CHỦ (MENU)
# =========================
@app.route("/")
def home():
    return render_template("index.html")

# =========================
# ROUTES CHO TRANSPOSITION
# =========================
@app.route("/transposition")
def transposition_page():
    return render_template("transposition.html")

@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    data = request.get_json()
    text = data.get("text", "")
    key = int(data.get("key", 2))
    
    cipher = TranspositionCipher()
    return jsonify({"result": cipher.encrypt_text(text, key)})

@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    data = request.get_json()
    text = data.get("text", "")
    key = int(data.get("key", 2))
    
    cipher = TranspositionCipher()
    return jsonify({"result": cipher.decrypt_text(text, key)})

# =========================
# ROUTES CHO ECC
# =========================
@app.route("/ecc")
def ecc_page():
    return render_template("ecc.html")

@app.route("/ecc/encrypt", methods=["POST"])
def ecc_encrypt():
    data = request.get_json()
    text = data.get("text", "")
    key = data.get("key", "")
    
    cipher = ECCCipher()
    return jsonify({"result": cipher.encrypt_text(text, key)})

@app.route("/ecc/decrypt", methods=["POST"])
def ecc_decrypt():
    data = request.get_json()
    text = data.get("text", "")
    key = data.get("key", "")
    
    cipher = ECCCipher()
    return jsonify({"result": cipher.decrypt_text(text, key)})

# =========================
# MAIN CHẠY SERVER
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)