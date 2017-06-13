from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html')

@app.route("/", methods=['POST'])
def validate_form():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    username_error = ''
    password_error = ''
    verify_error = ''


    if len(username)==0:
        username_error = "That's not a valid username"
    
    if len(password)==0:
        password_error = "That's not a valid password"
        
    if len(verify)==0 or verify != password:
        verify_error = "Passwords do not match"
        password = ''
        verify = ''
    
    return render_template('signup_form.html', username_error=username_error, password_error=password_error,verify_error=verify_error)

app.run()