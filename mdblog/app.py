

from flask import url_for
from flask import render_template
from flask import Flask
from .data_base import articless
from flask import request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key = b'\x1b@\xd3=\x03\xce3\xabJ<\t\xbd\x08\x17V\xae\xb8\xa3F\xdc\xf4\xb29\xb4'


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
        return redirect(url_for("login"))


@app.route("/logout/", methods=["POST"])
def logout():
    return redirect(url_for("login"))












