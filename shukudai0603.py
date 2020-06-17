# coding:utf-8
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


# http://localhost:5000/にリクエストが来たときの処理
@app.route("/")
def index():
   day = "現在日付検索"
   return render_template("day.html",day=day)


@app.route("/req")
def req():
    return render_template("request2.html",message="日付を入力してください")


@app.route('/res', methods=["POST"])
def res():
    today = datetime.date.today()
    today = str(today)
    date = request.form["date"]
    if today == date:
        return render_template("response2.html",message="日付が一致しています")
    else:
        return render_template("request2.html",message="日付が一致しません")

    # app.logger.info("post data: " + str(request.form.to_dict()))
    # da = str(datetime.date.fromisoformat(request.form['da']))
    # date = str(datetime.date.today())
    # app.logger.info(da)
    # app.logger.info(date)
    # return render_template("./response2.html", da=da,date=date)


if __name__ == "__main__":
    # webサーバーの立ち上げ
    app.run()