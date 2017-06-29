from loopDB import *
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify, make_response
from flask_socketio import SocketIO
import json
import base64
from cStringIO import StringIO

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'SECRET'

socketio = SocketIO(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='404'), 404

@app.errorhandler(500)
def internal_error(e):
	return render_template('500.html', title='500'), 500

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		instructions = request.form["instructions"]
		name = request.form["name"]
		resistance = request.form["resistance"]
		if instructions != "":
			session['instructions'] = instructions
			session['name'] = name
			session['resistance'] = resistance
			return redirect(url_for('plasmapo'))
		
	return render_template('home.html')

@app.route('/plasmapo')
def plasmapo():
	commands = []
	instructions = session.get('instructions')
	name = session.get('name')
	resistance = session.get('resistance')
	lines = instructions.splitlines()
	for line in lines:
		commands.append(line)
	return render_template('plasmapo.html', instructions = commands, name = name, resistance = resistance)

if __name__ == '__main__':
	socketio.run(app, debug=True,host='0.0.0.0', port = 8080)