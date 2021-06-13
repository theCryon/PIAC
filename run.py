from flask import Flask, request, render_template
from flask_mail import Mail, Message
from flask import abort, redirect, url_for, make_response

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mkrajnik225@gmail.com'
app.config['MAIL_PASSWORD'] = 'g2tra7!2CEhL'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/aboutme')
def about():
    return render_template('aboutme.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/send_message", methods=['GET', 'POST'])
def send_message():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        msg = request.form['message']

        message = Message(name, sender="mkrajnik225@gmail.com", recipients=[email])

        message.body = msg

        mail.send(message)
        success = "Message sent"

        return render_template("contact.html", success=success)

# @app.route('/error_denied')
# def error_denied():
#     abort(401)
#
#
# @app.route('/error_internal')
# def error_internal():
#     return render_template('template.html', name='ERROR 505'), 505
#
#
# @app.route('/error_not_found')
# def error_not_found():
#     response = make_response(render_template('template.html', name='ERROR 404'), 404)
#     response.headers['X-Something'] = 'A value'
#     return response
#
#
# @app.errorhandler(404)
# def not_found_error(error):
#     return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
