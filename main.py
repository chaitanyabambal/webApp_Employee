import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Hello</h1>"

@app.route("/contact")
def contact():
    return flask.render_template("contact.html")


@app.route("/contact")
def ContactUs():
    return render_template("Admin.html")


@app.route("/Search")
def Search():
    return render_template("Search.html")

@app.route("/delete")
def Delete():
    return render_template("delete.html")


if __name__ == "__main__":
    app.run()