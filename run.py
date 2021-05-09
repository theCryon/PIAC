from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/portfolio")
def portfolio():
    return "Portfolio"

@app.route("/contact")
def contact():
    return "Send email to me"

@app.route("/blog")
def blog():
    return "blog"

if __name__ == '__main__':
    app.run(debug=True)
