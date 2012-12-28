from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

# index view function supressed for brevity

@app.route('/lgin', methods = ['GET','POST'])
def login()
    form = LoginForm()
    return render_template('login.html',
        title = 'Sign In',
        form = form)

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Edgar' } # fake user
    posts = [ #fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in LA!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)
