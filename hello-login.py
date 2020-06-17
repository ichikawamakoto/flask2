# coding utf-8
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, logout_user
app = Flask(__name__)


# 追加
# セッションを使うためにシークレットキーが必要です
app.secret_key = 'secret key'

login_manager = LoginManager()
login_manager.init_app(app)

@app.route("/",methods=["GET"])
def form():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login():
    return redirect(url_for("dashboard"))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    # webサーバーの立ち上げ
    app.run()




