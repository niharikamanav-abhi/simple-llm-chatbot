"""
app.py  —  Step 3

The chat UI, built on top of chatbot.py from Step 2.

How to run this in VS Code:
  1. Make sure Step 2 (chatbot.py run directly) gave you a real reply.
  2. Open this file, click the "Run Python File" triangle button (or F5).
  3. Look at the terminal — it should say "Running on http://127.0.0.1:5000"
  4. Open that address in your browser and try chatting.
  5. To stop the server, click in the terminal and press Ctrl+C.
"""

from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or request.form
    user_message = data.get("message", "")
    reply = get_response(user_message)
    return jsonify({"response": reply})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=(port == 5000))