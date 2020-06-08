from flask import Flask

app = Flask(__name__)
@app.route("/",methods=["get","post"])
def index():
    return "hello python"

app.run()