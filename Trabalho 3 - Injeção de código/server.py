import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
@app.route('/echo')
def index():
	echo_input = {'echo':"Please make a GET request with '?echo=your_input'"}
	if request.args.get('echo'):
		echo_input['echo'] = request.args.get('echo')
	template = '''<h3>Echo: %s</h3>''' % echo_input['echo']
	return render_template_string(template, echo_input=echo_input)

app.jinja_env.globals['os'] = os

if __name__ == "__main__":
	app.run(debug=True)
