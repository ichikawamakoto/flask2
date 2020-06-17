from flask import Flask, render_template
app = Flask(__name__)

player = "勇者"

#メニューを表示

@app.route("/")
def menu():
    return render_template("menu.html",player=player)

#歩く
@app.route("/walk")
def walk():
    message = player + "は広野を歩いていた"
    return render_template("action.html",player= player,message=message)

@app.route("/attack")
def attack():
    message = player + "はモンスターを攻撃した"
    return render_template("action.html",player=player,message=message)
