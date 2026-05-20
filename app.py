from flask import Flask, jsonify
import os


app = Flask(__name__)

@app.route("/")
def home():
    return "Version 2 Deployed 🚀"

@app.route("/products")
def products():
    return jsonify([
        {"id": 1, "name": "Shirt", "price": 500},
        {"id": 2, "name": "Shoes", "price": 1200}
    ])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)