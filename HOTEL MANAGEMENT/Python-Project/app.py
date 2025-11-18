from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__,template_folder='templates')

@app.route('/')
def Main():
    return render_template('Main.html')

@app.route('/Login')
def Login():
    return render_template('Login.html')

@app.route('/Home')
def Home():
    return render_template('Main.html')

@app.route('/Signup')
def Signup():
    return render_template('Signup.html')

@app.route('/Rooms')
def Rooms():
    return render_template('Rooms.html')

@app.route('/Tables')
def Tables():
    return render_template('Tables.html')

@app.route('/Checkin')
def Checkin():
    return render_template('checkin.html')

@app.route('/Checkout')
def Checkout():
    return render_template('checkout.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)