from flask import Flask, request, render_template

app = Flask(__name__)

print (__name__)

@app.route('/')
def index():
	return "index page"

@app.route('/hello/')
def hello():
	return "hello world!"

@app.route('/hello/<username>')
def hello_user(username):
	return "hello %s" % username


@app.route('/hellot/<name>')
def hello_temp(name=None):
	return render_template('hello.html', name = name)
