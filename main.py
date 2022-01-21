from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    pass


if __name__ == "__main__":
    app.run(host="192.168.0.15", port=5000)
