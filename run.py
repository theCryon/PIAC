from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for, make_response

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/aboutme')
def about():
    return render_template('aboutme.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == "POST":
#         return request.form["username"]+"+"+request.form["password"]
#     else:
#         return render_template('login.html')
#
# @app.route('/user/<username>', methods=['GET','POST'])
# def show_user_profile(username):
#     if request.method == 'POST':
#         return 'HTTP POST for user %s with password %s' % (username, request.form['password'])
#     else:
#         return 'HTTP GET for user %s' % username
#
@app.route('/error_denied')
def error_denied():
    abort(401)


@app.route('/error_internal')
def error_internal():
    return render_template('template.html', name='ERROR 505'), 505


@app.route('/error_not_found')
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404)
    response.headers['X-Something'] = 'A value'
    return response


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
