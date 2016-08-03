from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	#return 'Hello, World'
	user = {'nickname': 'Miguel'}
	posts = [
        {
            'author': { 'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan'},
            'body': 'The Avenger movie was so cool!'
        }
    ]

	return render_template('index.html', user = user, posts = posts)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for OpenID="' + form.openid.data + '", remember_me=' + str(form.rememberme.data))
        return redirect('/index')
    return render_template('login.html',
            title = 'Sigin In',
            form = form,
            providers = app.config['OPENID_PROVIDERS'])
