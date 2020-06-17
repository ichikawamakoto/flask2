from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "flask"
    players = ["勇者","魔法使い","盗賊","戦士"]
    return render_template("index.html", name=name,players=players)

@app.route("/about")
def about():
    return render_template("index.html")

