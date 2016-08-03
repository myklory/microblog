from flask import render_template
from app import app

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
