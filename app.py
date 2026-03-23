from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to vulnerable app"

@app.route("/ping")
def ping():
    host = request.args.get("host")
    return os.popen(f"ping -c 1 {host}").read()

API_KEY = "12345-SECRET-KEY"

if __name__ == "__main__":
    app.run(debug=True)
