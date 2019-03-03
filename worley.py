from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/events')
def events():
	return render_template('events.html')


@app.route('/experience')
def experience():
	return render_template('experience.html')


@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

