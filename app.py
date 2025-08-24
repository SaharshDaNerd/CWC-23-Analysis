from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/plot/<name>")
def plot(name):
    return send_from_directory("templates", f"{name}.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
