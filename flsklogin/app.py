from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import os



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db=SQLAlchemy(app)
app.config['SECRET_KEY'] = 'thisisasecretkey'


class user(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80),nullable=False, unique=True)
    password=db.Column(db.String(80),nullable=False)



    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")


if __name__ =="__main__":
    app.run(debug=True)
    
with app.app_context(): 
    db.create_all()