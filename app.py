from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def hello_world():
    return "Hello, world!\n", 200, {"Content-Type": "text/plain; charset=utf-8"}


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    # Keep the first version local-only. Later, we will configure a network-facing host.
    app.run(host="127.0.0.1", port=5000, debug=False)
