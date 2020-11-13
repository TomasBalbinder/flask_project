


from flask import render_template
from flask import Flask


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

@app.route("/")
def back():
    return render_template("index.html")