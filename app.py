
from flask import Flask, render_template, request,redirect,session
from db import Database

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
dbo = Database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def index1():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('aboutpage1.html')

@app.route('/how')
def how():
    return render_template('howitworks1.html')

@app.route('/book')
def book():
    return render_template('book.html')


@app.route("/book_session",methods=['post'])
def book_session():
    name = request.form.get("user_name")
    email = request.form.get("user_email")
    age = request.form.get("user_age")
    education = request.form.get("user_edu")
    clg = request.form.get("user_clg")
    year = request.form.get("user_year")
    day = request.form.get("user_day")

    response = dbo.insert(name,email,age,education,clg,year,day)
    if response:
        return render_template('book.html',message='Your session is booked')
    else:
        return render_template('book.html',message='Email already exists or The day you are looking for is already booked')

app.run(debug=True)


