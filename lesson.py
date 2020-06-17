import sqlite3

from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response


app = Flask(__name__)


def get_db():
    db = getattr(g,"_database",None)
    if db is None:
        db = g._database = sqlite3.connect("test_sqlite.db")
        return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g,"_database",None)
    if db is not None:
        db.close()

@app.route("/employee",methods=["POST","PUT","DELETE"])
@app.route("/employee/<name>",methods=["GET"])
def employee(name=None):
    if request.method == "GET":
        return name
        db = get_db()
        curs = db_cursor()
        curs.execute(
            ""
        )





@app.route("/")
def hello_world():
    return "top"

@app.route("/hello/<name>")
@app.route("/hello")
def hello_world2(name=None):
    # return "hello_world {}".format(name)
    return render_template("hello.html",name=name)

@app.route("/post",methods=["POST","PUT","DELETE"])
def show_post():
    return str(request.values["name"])

def main():
    app.debug = True
    app.run()

if __name__ == "__main__":
    main()
