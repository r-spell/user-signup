from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html')

def string_invalid(string):
    if len(string)<3 or len(string)>20 or ' ' in string:
        return True
    return False

def email_invalid(string):
    if string_invalid(string):
        return True
    if string.count('@') != 1 or string.count('@') != 1 :
        return True
    return False

@app.route("/", methods=['POST'])
def validate_form():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''


    if string_invalid(username):
        username_error = "That's not a valid username"
        username = ''

    if string_invalid(password):
        password_error = "That's not a valid password"
        password = ''

    if password_error or verify != password:
        verify_error = "Passwords do not match"
        password = ''
        verify = ''
    
    if email != '':
        if email_invalid(email):
            email_error = "That's not a valid email"
    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('welcome?username={0}'.format(username))
    else:
        return render_template('signup_form.html', username_error=username_error, password_error=password_error,verify_error=verify_error, email_error=email_error)

@app.route('/welcome')
def welcome():
    return "TEST"

app.run()