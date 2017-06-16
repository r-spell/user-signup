from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html')

# Check if length of string is valid.  Returns True if Invalid.
def string_invalid(string):
    if len(string)<3 or len(string)>20 or ' ' in string:
        return True
    return False

#check if string is valid length and only one @ sign.
def email_invalid(string):
    if string_invalid(string):
        return True
    # check exactly one @ sign
    if string.count('@') != 1:
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

    # tests to show error and clear input if entry is invalid
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
    
    # show welcome page if no errors
    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('welcome?username={0}'.format(username))
    # show errors on signup page if any errors
    else:
        return render_template('signup_form.html', username_error=username_error, password_error=password_error,verify_error=verify_error, email_error=email_error)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()