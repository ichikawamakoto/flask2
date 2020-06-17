from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def show():
    message = "hello world"
    return render_template("form.html",message=message)

@app.route("/result",methods=["POST"])
def result():
    message = "This is paiza"
    article = request.form["article"]
    name = request.form["name"]
    return render_template("form.html",message=message,article=article,name=name)


if __name__ == "__main__":
    app.run()
