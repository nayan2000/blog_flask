from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nayan'}
    posts = [
        {
            'author': {'username' : 'John'},
            'body': 'I am so cooool'
        },
        {
            'author': {'username' : 'Nayan'},
            'body': 'The Glass is full of water.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

#Jinja2 templates preloaded in flask