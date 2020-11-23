

from flask import url_for
from flask import render_template
from flask import Flask
from .data_base import articless
from flask import request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key = b'7H{&\xa3\x92\xed\x86\xbe\xd4\x06U\xb1\x87s\xeb\x12Q\xd7\xf8Z/j\x92'

@app.route("/")
def welcome_page():
    return render_template("index.html")

@app.route("/admin/")
def admin():
    if "logged" not in session:
        return redirect(url_for("login"))
    else:
        return render_template("admin.html")



@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/articles/")
def articles():
    return render_template("articles.html", articles=articless.items())


@app.route("/articles/<int:art_id>")
def article(art_id):
    article = articless.get(art_id)
    if article:
        return render_template("article.html", article=article)
    return render_template("notfound.html", id=art_id)


@app.route("/login/", methods=["GET"])
def login():
        return render_template("login.html")


@app.route("/login/", methods=["POST"])
def login_user():
    username = request.form["username"]
    password = request.form["password"]
    if username == "admin" and password == "admin":
        session["logged"]=True
        return redirect(url_for("admin"))

    else:
        return render_template("fail_login.html")

@app.route("/logout/", methods=["POST"])
def logout():
    session.pop("logged")
    return redirect(url_for("welcome_page"))















