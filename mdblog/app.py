


from flask import render_template
from flask import Flask
from .data_base import articless

app = Flask(__name__)

@app.route("/")
def welcome_page():
    return render_template("index.html")

@app.route("/admin/")
def admin():
    return render_template("admin.html")


@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/articles/")
def articles():
    return render_template("articles.html", articles=articless.items())


@app.route("/articles/<int:art_id>")
def article(art_id):
    article = articless[art_id]
    return render_template("article.html", article=article)










