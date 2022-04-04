
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to my website"
@app.route("/")

@app.route("/contact")
def ContactPage():
    return render_template()
@app.route("/Home")
def Home():
    return "Home Page"
@app.route("/Gallary")
def Gallary():
    return " gallary"
if __name__ == '__main__':
    app.main()