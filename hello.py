from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route("/")
def get_index():
    me ="Anthony"
    return f"<p>Hello {me}, fire in the hole!</p>"

@app.route("/hello")
def get_hello():
    me ="Anthony"
    return f"<p>Hello {me}, World!</p>"

@app.route("/goodbye")
def get_goodbye():
    me ="Anthony"
    return f"<p>Bye {me}, come back soon!</p>"

@app.route("/data")
def get_data():
    data = [
        ("name:Freddy", "type:bear"),
        ("name:Bonnie", "type:bunny"),
        ("name:Chica", "type:kitchen"),
        ("name:Foxy", "type:pirate"),
        ("name:Gabe", "type:colossal")
    ]
    return jsonify(data);
@app.route("/api/status")
def get_status():
    data = [
        ("name:Freddy", "type:bear"),
        ("name:Bonnie", "type:bunny"),
        ("name:Chica", "type:kitchen"),
        ("name:Foxy", "type:pirate"),
        ("name:Gabe", "type:colossal")
    ]
    return jsonify(data)
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory('.',path)
