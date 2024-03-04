from flask import Flask, jsonify, render_template
from mongita import MongitaClientDisk

app = Flask(__name__)

@app.route("/")
def get_index():
    me ="Anthony"
    return f"<p>Hello {me}, fire in the hole!</p>"

@app.route("/goodbye")
def get_goodbye():
    me ="Anthony"
    return f"<p>Bye {me}, come back soon!</p>"

@app.route("/data")
def get_data():
    data = [

    ]
    return jsonify(data);
@app.route("/api/status")
def get_status():
    data = [

    ]
    return jsonify(data)

@app.route("/hello")
def get_hello():
    return render_template("helloworld.html")
@app.route("/hello2/<name>")
def get_hello2():
    return render_template("helloworld.html")

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory('.',path)
