

from flask import url_for
from flask import render_template
from flask import Flask
from flask import request
from flask import redirect
from flask import session
from flask import g
import sqlite3
from flask import flash


DATABASE = "blog.db"

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

@app.route("/articles/", methods=["GET"])
def articles():
    db = get_db()
    cur = db.execute("select * from articles order by id desc")
    articles = cur.fetchall()
    return render_template("articles.html", articles=articles)

@app.route("/articles/", methods=["POST"])
def add_articles():
    db = get_db()
    db.execute("insert into articles (title, content) values (?, ?)",[request.form.get("title"), request.form.get("content")])

    db.commit()
    return redirect(url_for("articles"))


@app.route("/articles/<int:art_id>")
def article(art_id):
    db = get_db()
    cur = db.execute("select * from articles where id=(?)", [art_id])
    article = cur.fetchone()
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
        flash("Loggin Succesfull")
        return redirect(url_for("admin"))

    else:
        flash("wrong login")
        return redirect(url_for("login"))

@app.route("/logout/", methods=["POST"])
def logout():
    session.pop("logged")
    flash("Logout Success")
    return redirect(url_for("welcome_page"))



def connect_db():
    rv = sqlite3.connect("DATABASE")
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    if not hasattr(g, "sqlite_db"):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "sqlite_db"):
        g.sqlite_db.close()


def init_db(appp):
    with appp.app_context():
        db = get_db()
        with open("mdblog/schema.sql", "r") as fp:
            db.cursor().executescript(fp.read())
        db.commit()















